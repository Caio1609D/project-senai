import sys
sys.path.append('/tools')
import tools.db as db

def main():
    username = input("Insira seu novo nome de usuário:\n")
    password = input("Insira sua nova senha:\n")

    db.create_user(username, password)

if __name__ == "__main__":
    main()