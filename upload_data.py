import pymongo
import json
import ast
from pymongo import MongoClient

print("Leyendo el CSV")

client_cloud = MongoClient('mongodb://root:Calamardo99!@localhost:27017')

db = client_cloud.ShareBoardGames
games = db.games

df = pd.read_csv("path/to/boardgames1.csv")

print("Cargando los datos a mongoDB")

json_games = df.to_json(orient="records")
records = json.loads(df.T.to_json()).values()

games.insert(records)

print("###################")
print("### Listo Listo ###")
print("###################")