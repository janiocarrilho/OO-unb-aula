# import consumer
# from models import Filme

# response = consumer.buscarFilme(input("Digite o nome do Filme: "))
# print(len(response['results']))


# filme = response['results'][0]
# print(filme)
# print("----------------------------------------------")
# print(consumer.detalhesFilme(filme['id']))
# detalhes_filme = consumer.detalhesFilme(filme['id'])

# print("------------------TESTE------------------")


# def generos(lista):
#     gens = []
#     for genero in lista:
#        gens.append(genero['name'])
    
#     return ", ".join(gens)

# filme_classe = Filme(filme['original_title'], filme['release_date'], generos(detalhes_filme['genres']))
# print(filme_classe.to_dict())


# print("------------------TESTE------------------")

# if len(response['results']) > 0:
#     print("Qual desses você ira adicionar ?")
#     opcoes = []
#     for i in range(len(response['results'])):
#         opcoes.append(i+1)
#         print(f"{i+1} - {response['results'][i]['original_title']}")
#     escolhida = int(input("Digite o número: "))
#     print(response['results'][escolhida-1]['original_title'])