import consumer
from models import Filme


def procura_adiciona(titulo: str) -> Filme:
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
        data = response['results'][0]

    detalhes_data = consumer.detalhesFilme(filme['id'])

    filme = Filme(filme['original_title'], filme['release_date'], generos(detalhes_data['genres']))

    return filme


def generos(lista):
    gens = []
    for genero in lista:
       gens.append(genero['name'])
    
    return ", ".join(gens)