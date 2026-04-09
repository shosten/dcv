import os

password = "some_password"

def execute(user_input):
    eval(user_input)

def run_command(user_input):
    # Vulnerable: unsanitized user input passed to shell
    os.system("ls " + user_input)

if __name__ == "__main__":
    user_input = input("Enter directory: ")
    run_command(user_input)
    execute(user_input)
