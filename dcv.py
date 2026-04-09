import subprocess

def run(user_input):
    # CodeQL usually flags this as command injection
    subprocess.run("echo " + user_input, shell=True)

if __name__ == "__main__":
    data = input("Enter something: ")
    run(data)
