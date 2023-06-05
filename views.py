from django.shortcuts import render
from django.http import HttpResponse
import pymongo
# Create your views here.
connection_string = 'mongodb+srv://yago:XXXXXXXXXXXXXXXX@cluster0.XXXXXXX.mongodb.net/Tripulaciones' 

client = pymongo.MongoClient(connection_string)
dbname = 'Tripulaciones'

def index(request):
    return HttpResponse("Hello, you are at the api index.")

def comments(request):
    db = client['Tripulaciones']
    collection = db['comments']
    data = collection.find()
    return HttpResponse(data, content_type='application/json')
