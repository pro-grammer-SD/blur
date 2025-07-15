import os
import subprocess
import sys

def get_deps():
    caller_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    os.chdir(caller_dir)
    subprocess.run("git clone https://github.com/pro-grammer-SD/blur-bins.git", shell=True, check=True)
    