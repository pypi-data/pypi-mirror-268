import os
import configparser
import subprocess
from subprocess import Popen, PIPE
import argparse
import sys

class Lock:

    extensions = ["py", "c", "cpp", "h", "hpp", "java", "js", "ts", "txt", "hs"]
    lock_folders = ["src"]
    lock_files = "solver"

    def __init__(self):
        self.password = None
        self.config_file = None
        self.load_config_file(".")
        self.load_password()
        self.default_file = "feno.lock"

    # from hero to root, search for the feno.lock file
    # and return the path to it
    def load_config_file(self, init) -> str:
        path = os.path.abspath(init)
        while path != '/':
            if os.path.exists(path + "/feno.lock"):
                self.config_file = path + "/feno.lock"
                return self.config_file
            path = os.path.dirname(path)
        print("fail: file feno.lock not found")
        return None

    def load_password(self):
        if self.config_file is None:
            print("fail: config file not loaded")
            sys.exit(1)
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.password = config["DEFAULT"]["pass"]
    
    def verify(self, path):
        if self.password is None:
            print("fail: password not loaded")
            sys.exit(1)
        if not os.path.exists(path):
            print("fail: file not found")
            sys.exit(1)

    def lock_file(self, path):
        self.verify(path)
        # run subprocess to create the lock file passing the password as stdin
        cmd = "gpg --batch -c --passphrase-fd 0 " + path 
        answer = subprocess.run(cmd, input=self.password, stdout=PIPE, stderr=PIPE, text=True, shell=True)
        os.remove(path)

    @staticmethod
    def is_inside_a_dot_dir(path):
        for piece in path.split(os.sep):
            if piece.startswith("."):
                return True
        return False

    @staticmethod
    def match_lock_pattern(path):
        folders = path.split(os.sep)[:-1]
        file = path.split(os.sep)[-1]
        if not file.split(".")[-1] in Lock.extensions:
            return False
        for piece in folders:
            if piece in Lock.lock_folders:
                return True
        if Lock.lock_files in file.lower():
            return True
        return False
    
    @staticmethod
    def match_unlock_pattern(path):
        file = path.split(os.sep)[-1]
        if file.split(".")[-1] == "gpg":
            return True
        return False

    # walk recursively through the folders and lock all files
    def lock_folder(self, path):
        found = False
        
        for root, _dirs, files in os.walk(path):
            for file in files:
                path = os.path.normpath(os.path.join(root, file))
                if Lock.is_inside_a_dot_dir(path):
                    continue
                elif Lock.match_lock_pattern(path):
                    print(file, end=" ", flush=True)
                    self.lock_file(path)
                    found = True
        if found:
            print("")
    
    
    def unlock_file(self, path):
        self.verify(path)
        # run subprocess to create the lock file passing the password as stdin
        cmd = "gpg --batch -d --passphrase-fd 0 " + path
        answer = subprocess.run(cmd, input=self.password, stdout=PIPE, stderr=PIPE, text=True, shell=True)
        # remove .gpg extension
        if answer.returncode != 0:
            print(answer.stderr)
            sys.exit(1)
        else:
            target = path[:-4]
            with open(target, "w") as f:
                f.write(answer.stdout)
            os.remove(path)    

    def unlock_folder(self, path):
        found = False
        for root, dirs, files in os.walk(path):
            for file in files:
                path = os.path.normpath(os.path.join(root, file))
                if Lock.is_inside_a_dot_dir(path):
                    continue
                elif Lock.match_unlock_pattern(path):
                    print(file, end=" ", flush=True)
                    self.unlock_file(path)
                    found = True
        if found:
            print("")


def lock():
    parser = argparse.ArgumentParser(description='Lock files')
    parser.add_argument("targets", type=str, nargs="+", help='files to lock')
    args = parser.parse_args()
    lock = Lock()
    for target in args.targets:
        if os.path.isdir(target):
            lock.lock_folder(target)
        else:
            lock.lock_file(target)

def unlock():
    parser = argparse.ArgumentParser(description='Unlock files')
    parser.add_argument('targets', type=str, nargs="+", help='file to unlock')
    args = parser.parse_args()
    lock = Lock()
    for target in args.targets:
        if os.path.isdir(target):
            lock.unlock_folder(target)
        else:
            lock.unlock_file(target)






