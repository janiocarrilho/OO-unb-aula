import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017/")
db = client["recomendacao_filmes"]
usuarios_collection = db["usuarios"]
filmes_collection = db["filmes"]

