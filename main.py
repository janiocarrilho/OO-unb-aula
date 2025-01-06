from models import Usuario
from views import view


def main():
    username = input("Digite seu Username: ")
    user = Usuario(username)
    user.cadastrar_user()

    while True:
        view(user)


if __name__ == "__main__":
    main()