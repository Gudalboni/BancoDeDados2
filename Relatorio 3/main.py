from database import Database
from pokedex import Pokedex

# Instanciando a classe Database
db = Database(database="pokedex", collection="pokemons")

# Instanciando a classe Pokedex com a instância do Database
pokedex = Pokedex(db)

# Realizando as consultas e gerando os logs
pokedex.query1()
pokedex.query2()
pokedex.query3()
pokedex.query4()
pokedex.query5()