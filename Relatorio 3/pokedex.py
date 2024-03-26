from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def query1(self):
        data = self.database.collection.find({"type": "Grass"})
        writeAJson(data, "query1_log")

    def query2(self):
        data = self.database.collection.find({"generation": 1})
        writeAJson(data, "query2_log")

    def query3(self):
        data = self.database.collection.find({"type": "Fire", "generation": {"$gt": 3}})
        writeAJson(data, "query3_log")

    def query4(self):
        data = self.database.collection.find().sort("name", 1).limit(10)
        writeAJson(data, "query4_log")

    def query5(self):
        data = self.database.collection.aggregate([
            {"$group": {"_id": "$type", "total": {"$sum": 1}}}
        ])
        writeAJson(data, "query5_log")
