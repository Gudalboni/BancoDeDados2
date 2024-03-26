from pymongo import MongoClient

class ProductAnalyzer:
    def __init__(self, uri, database, collection):
        self.client = MongoClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    def total_vendas_por_dia(self):
        """Retorna o total de vendas por dia."""
        pipeline = [
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": 1}}}
        ]
        return list(self.collection.aggregate(pipeline))

    def produto_mais_vendido(self):
        """Retorna o produto mais vendido em todas as compras."""
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_vendido": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_vendido": -1}},
            {"$limit": 1}
        ]
        return list(self.collection.aggregate(pipeline))

    def cliente_mais_gastou(self):
        """Encontra o cliente que mais gastou em uma única compra."""
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id", "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ]
        return list(self.collection.aggregate(pipeline))

    def produtos_quantidade_acima_de_um(self):
        """Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidade."""
        pipeline = [
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {"$group": {"_id": "$produtos.descricao", "quantidade_vendida": {"$sum": "$produtos.quantidade"}}}
        ]
        return list(self.collection.aggregate(pipeline))

    def __del__(self):
        self.client.close()

# Exemplo de uso:
if __name__ == "__main__":
    # Configurações do MongoDB
    uri = "mongodb://localhost:27017/"
    database = "mercado"
    collection = "compras"

    # Instanciar a classe ProductAnalyzer
    analyzer = ProductAnalyzer(uri, database, collection)

    # Exemplos de chamada de métodos da classe
    print("Total de vendas por dia:")
    print(analyzer.total_vendas_por_dia())

    print("\nProduto mais vendido:")
    print(analyzer.produto_mais_vendido())

    print("\nCliente que mais gastou:")
    print(analyzer.cliente_mais_gastou())

    print("\nProdutos com quantidade vendida acima de 1 unidade:")
    print(analyzer.produtos_quantidade_acima_de_um())