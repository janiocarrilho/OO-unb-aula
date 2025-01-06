import consumer
from models import Filme


def procura_adiciona(titulo: str):
    response = consumer.buscarFilme(titulo)

    if len(response['results']) > 0:
        print("Qual desses você ira adicionar ?")
        opcoes = []
        for i in range(len(response['results'])):
            opcoes.append(i+1)
            print(f"{i+1} - {response['results'][i]['original_title']}")
        escolhida = int(input("Digite o número: "))
        data = response['results'][escolhida-1]
    else:
        return None

    detalhes_data = consumer.detalhesFilme(data['id'])

    filme = Filme(data['original_title'], data['release_date'], generos(detalhes_data['genres']))

    return filme


def generos(lista):
    gens = []
    for genero in lista:
       gens.append(genero['name'])
    
    return ", ".join(gens)