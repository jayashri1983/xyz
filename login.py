import os

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    os.system(f"echo {username}:{password} >> users.txt")  # 🚨 Unsafe

if __name__ == "__main__":
    login()
