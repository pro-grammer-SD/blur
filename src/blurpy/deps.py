import subprocess

def get_deps():
    subprocess.run("git clone https://github.com/pro-grammer-SD/blur-bins.git", shell=True, check=True)
    