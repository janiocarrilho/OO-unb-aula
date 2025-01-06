import controller
from models import Usuario


def view(user: Usuario):
    print("\n--- MENU ---")
    print("1. Adicionar filme")
    print("2. Listar meus filmes")
    print("3. Recomendar filme aleatório")
    print("4. Remover filme")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        filme = controller.procura_adiciona(input("Digite o nome do Filme: "))
        user.adicionar_filme(filme)

    elif escolha == "2":
        print("\n--- Minha Lista de Filmes ---")
        filmes = user.listar_filmes()
        if filmes:
            for filme in filmes:
                print(filme)
        else:
            print("Sua lista de filmes está vazia!")

    elif escolha == "3":
        filme = user.recomendar_aleatorio()
        if filme:
            print("\n--- Filme Recomendado Aleatoriamente ---")
            print(f"Título: {filme['titulo']}, Ano: {filme['ano']}, Gênero: {filme['genero']}")

    elif escolha == "4":
        titulo = input("Digite o título do filme que deseja remover: ")
        user.remover_filme(titulo)

    elif escolha == "5":
        print("Saindo... Até logo!")
        return False

    else:
        print("Opção inválida!")