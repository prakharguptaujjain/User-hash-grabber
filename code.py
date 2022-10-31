from sys import platform
import subprocess
import os


def linuxhash():
    """Extracting hash for Linux OS"""
    installjohn = "sudo apt-get install -y john"
    print(subprocess.check_output(installjohn, shell=True))
    subprocess.check_output("sudo unshadow /etc/passwd /etc/shadow > hash.txt")

    if (os.path.exists("./hash.txt") and os.path.getsize("./hash.txt") > 0):
        print("Process done successfully")
        print("Hashes saved in hash.txt")
    else:
        print("Process failed")


def windowshash():
    """Extracting hash for Windows OS"""
    print("Currently inavailable for Windows OS")


if __name__ == "__main__":
    if platform == "linux" or platform == "linux2":
        linuxhash()
    elif platform == "darwin":
        print("Mac OS currently not supported")
    elif platform == "win32":
        windowshash()
    else:
        print("OS currently not supported")
