from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import pymongo
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.ShareBoardGames
games = db.games

def retrieve_all(request, limit):
    #Retorna todos los documentos
    #games = db[doc]
    result=[]
    for x in games.find():
        del x['_id']
        result.append(x)
    result = result[:limit]    
    result = json.dumps(result)
    return HttpResponse(result)