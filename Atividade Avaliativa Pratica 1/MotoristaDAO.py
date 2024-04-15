from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, db):
        self.database = db
        self.collection = self.database.collection  # Referência à coleção

    def createMotorista(self, nome: str, nota: int):
        try:
            resultado = self.collection.insert_one({"nome": nome, "nota": nota})
            print(f"Novo motorista cadastrado com sucesso. ID: {resultado.inserted_id}")
            return resultado.inserted_id
        except Exception as e:
            print(f"Erro ao cadastrar motorista: {e}")
            return None

    def readMotoristaById(self, motoristaId: str):
        try:
            resultado = self.collection.find_one({"_id": ObjectId(motoristaId)})
            if resultado:
                print(f"Motorista encontrado: {resultado}")
            else:
                print("Nenhum motorista encontrado com o ID fornecido.")
            return resultado
        except Exception as e:
            print(f"Erro ao buscar motorista: {e}")
            return None

    def updateMotorista(self, motoristaId: str, nome: str, nota: int):
        try:
            resultado = self.collection.update_one({"_id": ObjectId(motoristaId)}, {"$set": {"nome": nome, "nota": nota}})
            print(f"Dados do motorista atualizados. Documentos modificados: {resultado.modified_count}")
            return resultado.modified_count
        except Exception as e:
            print(f"Erro ao atualizar motorista: {e}")
            return None

    def deleteMotorista(self, motoristaId: str):
        try:
            resultado = self.collection.delete_one({"_id": ObjectId(motoristaId)})
            print(f"Motorista removido com sucesso. Documentos deletados: {resultado.deleted_count}")
            return resultado.deleted_count
        except Exception as e:
            print(f"Erro ao remover motorista: {e}")
            return None
