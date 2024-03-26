from pymongo import MongoClient

# Conexão com o banco de dados
client = MongoClient("mongodb://localhost:27017/")
db = client["relatorio_5"]

# Questao 1
db.create_collection(
    "Livros",
    validator={
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["_id", "titulo", "autor", "ano", "preco"],
            "properties": {
                "_id": {"bsonType": ["int", "string"]},
                "titulo": {"bsonType": "string"},
                "autor": {"bsonType": "string"},
                "ano": {"bsonType": "int"},
                "preco": {"bsonType": "double"}
            }
        }
    }
)

# Questao 2
def menu():
    print("Menu:")
    print("1. Criar novo livro")
    print("2. Ler livro por ID")
    print("3. Atualizar livro")
    print("4. Deletar livro por ID")
    print("0. Sair")

def criar_livro():
    _id = input("Digite o ID do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    ano = int(input("Digite o ano do livro: "))
    preco = float(input("Digite o preço do livro: "))
    livro = {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}
    db.Livros.insert_one(livro)
    print("Livro criado com sucesso.")

def ler_livro_por_id():
    _id = input("Digite o ID do livro: ")
    livro = db.Livros.find_one({"_id": _id})
    print("Livro encontrado:" if livro else "Livro não encontrado.")
    print(livro) if livro else None

def atualizar_livro():
    _id = input("Digite o ID do livro que deseja atualizar: ")
    livro = db.Livros.find_one({"_id": _id})
    if livro:
        titulo = input("Digite o novo título do livro: ")
        autor = input("Digite o novo autor do livro: ")
        ano = int(input("Digite o novo ano do livro: "))
        preco = float(input("Digite o novo preço do livro: "))
        db.Livros.update_one({"_id": _id}, {"$set": {"titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
        print("Livro atualizado com sucesso.")
    else:
        print("Livro não encontrado.")

def deletar_livro_por_id():
    _id = input("Digite o ID do livro que deseja deletar: ")
    livro = db.Livros.find_one({"_id": _id})
    if livro:
        db.Livros.delete_one({"_id": _id})
        print("Livro deletado com sucesso.")
    else:
        print("Livro não encontrado.")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        criar_livro()
    elif opcao == "2":
        ler_livro_por_id()
    elif opcao == "3":
        atualizar_livro()
    elif opcao == "4":
        deletar_livro_por_id()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")