from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
import ast
from . import tasks

#################################
######### HTTP Requests #########
#################################

def ping(request):
    return HttpResponse("pong")

def retrieve_all(request):
    # Retorna todos los documentos    
    limit = int(request.GET["limit"])
    result = tasks.retrieve_games(limit)   
    result = json.dumps(result)
    return HttpResponse(result)

def retrieve_categories(request):
    limit = int(request.GET["limit"])
    games_list = tasks.retrieve_games(20)
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
    game_list = tasks.retrieve_games(limit)
    result = []
    for game in game_list:
        temp_game_categ = ast.literal_eval(game["boardgamecategory"])
        if category in temp_game_categ:
            result.append(game)
    result = json.dumps(result)            
    return HttpResponse(result)      

def games_by_categories(request):
    limit = int(request.GET["limit"])
    categories = request.GET.getlist("categories[]")
    result = tasks.games_and_categories(limit, categories)
    result = json.dumps(result)            
    return HttpResponse(result)          

def search_by_name(request):   
    limit = int(request.GET["limit"])
    game_name = str(request.GET["game_name"])
    result = tasks.search_by_name(limit, game_name)    
    result = json.dumps(result)    
    return HttpResponse(result)
