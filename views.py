import controller
from models import Usuario


def view(user: Usuario):
    while True:
        print("\n--- MENU ---")
        print("1. Adicionar filme")
        print("2. Listar meus filmes")
        print("3. Recomendar filme aleatório")
        print("4. Remover filme")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            filme = controller.procura_adiciona(input("Digite o nome do Filme: "))
            if filme:
                user.adicionar_filme(filme)
            else:
                print("Filme não encontrado")
                print()

        elif escolha == "2":
            print("\n--- Minha Lista de Filmes ---")
            filmes = user.listar_filmes()
            if filmes:
                for filme in filmes:
                    print(filme)
                    print()
            else:
                print("Sua lista de filmes está vazia!")

        elif escolha == "3":
            filme = user.recomendar_aleatorio()
            if filme:
                print("\n--- Filme Recomendado Aleatoriamente ---")
                print(f"Título: {filme['titulo']}, Data de Lançamento: {filme['data_lancamento']}, Gênero: {filme['generos']}")

        elif escolha == "4":
            titulo = input("Digite o título do filme que deseja remover: ")
            user.remover_filme(titulo)

        elif escolha == "5":
            print("Saindo... Até logo!")
            print()
            break

        else:
            print("Opção inválida!")
            print()