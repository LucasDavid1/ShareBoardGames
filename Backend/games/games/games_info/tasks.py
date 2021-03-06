from celery import shared_task
import pymongo
from pymongo import MongoClient
import ast

client = MongoClient('mongodb://root:Calamardo99!@localhost:27017')
db = client.ShareBoardGames
games = db.games

@shared_task
def retrieve_games(limit):
    # Retorna una cantidad de juegos
    games_list=[]
    for game in games.find():
        del game['_id']
        games_list.append(game)
    games_list = games_list[:limit]    
    return games_list

@shared_task()
def search_by_name(limit, game_name):
    result = []
    query = { "name": {"$regex" : f".*{game_name}.*"} }
    find_games = games.find(query)

    for game in find_games:
        del game['_id']
        result.append(game)
    return result[:limit]    

@shared_task()    
def games_by_category(limit, category):
    game_list = retrieve_games(limit)
    result = []
    for game in game_list:
        temp_game_categ = ast.literal_eval(game["boardgamecategory"])
        if category in temp_game_categ:
            result.append(game)
    return result   

@shared_task()    
def games_and_categories(limit, categories):    
    result = []
    for category in categories:
        result.append({"category": category, "games_getted": games_by_category(limit, category)})
    return result 