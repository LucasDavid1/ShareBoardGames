from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymongo
import json
from pymongo import MongoClient
import ast

client = MongoClient('localhost', 27017)
db = client.ShareBoardGames
games = db.games

#################################
####### Funciones locales #######
#################################

def retrieve_games(limit):
    # Retorna una cantidad de juegos
    games_list=[]
    for game in games.find():
        del game['_id']
        games_list.append(game)
    games_list = games_list[:limit]    
    return games_list

#################################
######### HTTP Requests #########
#################################

def ping(request):
    return HttpResponse("pong")

def retrieve_all(request):
    # Retorna todos los documentos    
    limit = int(request.GET["limit"])
    result = retrieve_games(limit)   
    result = json.dumps(result)
    return HttpResponse(result)

def retrieve_categories(request):
    limit = int(request.GET["limit"])
    games_list = retrieve_games(20)
    categories = []
    for game in games_list:
        temp_game_categ = ast.literal_eval(game["boardgamecategory"])
        categories.extend(temp_game_categ) # Se agregan las categorias del juego.
        categories = list(dict.fromkeys(categories)) # Se eliminan los elementos duplicados.        
    categories = categories[:limit]
    result = json.dumps(categories)
    return HttpResponse(result)

def games_by_category(request):
    limit = int(request.GET["limit"])
    category = str(request.GET["category"])
    game_list = retrieve_games(limit)
    result = []
    for game in game_list:
        temp_game_categ = ast.literal_eval(game["boardgamecategory"])
        if category in temp_game_categ:
            result.append(game)
    result = json.dumps(result)            
    return HttpResponse(result)      

def search_by_name(request, limit, game_name):   
    result = []
    query = { "name": {"$regex" : f".*{game_name}.*"} }
    find_games = games.find(query)

    for game in find_games:
        del game['_id']
        result.append(game)
    result = json.dumps(result)    
    return HttpResponse(result)
