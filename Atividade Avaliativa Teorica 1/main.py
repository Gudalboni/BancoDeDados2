import threading
import time
import random
from pymongo import MongoClient

# Função para gerar a temperatura aleatória entre 30 e 40 C°
def gerar_temperatura():
    return random.uniform(30, 40)

# Função para atualizar o banco de dados MongoDB
def atualizar_bd(nome_sensor, temperatura):
    cliente = MongoClient('localhost', 27017)  # Conexão com o servidor MongoDB
    db = cliente.bancoiot  # Acessando o banco de dados 'bancoiot'
    collection = db.sensores  # Acessando a coleção 'sensores'

    # Atualizando o documento do sensor no banco de dados
    collection.update_one({'nomeSensor': nome_sensor}, {'$set': {'valorSensor': temperatura}})

# Função para verificar se a temperatura é alta e atualizar o campo 'sensorAlarmado'
def verificar_alarme(nome_sensor, temperatura):
    if temperatura > 38:
        cliente = MongoClient('localhost', 27017)  # Conexão com o servidor MongoDB
        db = cliente.bancoiot  # Acessando o banco de dados 'bancoiot'
        collection = db.sensores  # Acessando a coleção 'sensores'

        # Atualizando o campo 'sensorAlarmado' para True
        collection.update_one({'nomeSensor': nome_sensor}, {'$set': {'sensorAlarmado': True}})
        print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome_sensor}!")

# Função principal para simular o sensor
def simular_sensor(nome_sensor, intervalo):
    while True:
        temperatura = gerar_temperatura()
        print(f"Sensor {nome_sensor}: Temperatura atual: {temperatura}°C")

        atualizar_bd(nome_sensor, temperatura)  # Atualizando o banco de dados
        verificar_alarme(nome_sensor, temperatura)  # Verificando se a temperatura é alta

        time.sleep(intervalo)

# Criando e iniciando as threads para cada sensor
sensor1_thread = threading.Thread(target=simular_sensor, args=('Temp1', 5))
sensor2_thread = threading.Thread(target=simular_sensor, args=('Temp2', 3))
sensor3_thread = threading.Thread(target=simular_sensor, args=('Temp3', 7))

sensor1_thread.start()
sensor2_thread.start()
sensor3_thread.start()