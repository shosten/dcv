import subprocess

def dangerous():
    user_input = input("cmd: ")
    subprocess.Popen(user_input, shell=True)

dangerous()
