import os
import sys
import subprocess


def TASK():
    bash_file = os.path.expanduser("~/.local/share/mytot/TASK")
    subprocess.run(["bash", bash_file] + sys.argv[1:], check=True)
