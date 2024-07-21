import os
import requests
from pymongo import MongoClient
from dotenv import load_dotenv
import json
from bson.json_util import dumps
# Conectar-se ao MongoDB Atlas
client = MongoClient("mongodb+srv://usuario:senha@cluster0.gd3uo2d.mongodb.net/meudb")
db = client["meudb"]
collection = db["product"]

# Definir o caminho para o arquivo JSON
JSON_FILE = "product.json"

# Realizar uma consulta na coleção
#result = collection.find({})

result = collection.find() 
  
# Converting cursor to the list  
# of dictionaries 
list_cur = list(result) 

# Converting to the JSON 
json_data = dumps(list_cur, indent = 2)  

# Writing data to file data.json 
with open(JSON_FILE, 'w') as file: 
    file.write(json_data)

print(f"Dados salvos no arquivo {JSON_FILE}")    