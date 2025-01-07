import random
import database as mongo

class Filme:
    def __init__(self, titulo, data_lancamento, genero):
        self.titulo = titulo
        self.data_lancamento = data_lancamento
        self.genero = genero

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "data_lancamento": self.data_lancamento,
            "generos": self.genero,
        }
    
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.id = None


    def cadastrar_user(self):
        user_existente = mongo.usuarios_collection.find_one({"nome": self.nome})
        if not user_existente:
            resultado = mongo.usuarios_collection.insert_one(({"nome": self.nome}))
            self.id = resultado.inserted_id
        else:
            self.id = user_existente["_id"]
    
    def adicionar_filme(self, filme: Filme):
        if not self.id:
            print("Usuario não cadastrado")
            return
        
        filme_data = filme.to_dict()
        mongo.usuarios_collection.update_one({"_id": self.id},{"$push": {"filmes" : filme_data}})
        print("Filme adicionado com sucesso")

    def listar_filmes(self):
        if not self.id:
            print("Usuário não salvo no banco de dados.")
            return []

        usuario = mongo.usuarios_collection.find_one({"_id": self.id})
        return usuario.get("filmes", [])
    
    def recomendar_aleatorio(self):
        if not self.id:
            print("Usuário não salvo no banco de dados.")
            return None

        usuario = mongo.usuarios_collection.find_one({"_id": self.id})
        filmes = usuario.get("filmes", [])

        if filmes:
            return random.choice(filmes)
        else:
            print("A lista de filmes está vazia!")
            return None
        
    def remover_filme(self, titulo):
        if not self.id:
            print("Usuário não salvo no banco de dados.")
            return

        resultado = mongo.usuarios_collection.update_one(
            {"_id": self.id},
            {"$pull": {"filmes": {"titulo": titulo}}}
        )
        if resultado.modified_count > 0:
            print(f"Filme '{titulo}' removido com sucesso!")
            print()
        else:
            print(f"Filme '{titulo}' não encontrado na lista.")
            print()

    

