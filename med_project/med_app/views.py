from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
from med_app.models import Pokemmon





#views

def index(request):
  response = json.dumps([{}])
  return HttpResponse(response, content_type = 'text/json')



@csrf_exempt
def add_pokemon(request):
  if request.method == 'POST':
    payload = json.loads(request.body)
    p_name = payload['name']
    p_hp = payload['hp']
    pokemon = Pokemmon(name = p_name, hp = p_hp)
    try:
      pokemon.save()
      response = json.dumps([{
        'Success': 'Pokemon Added Sucessfully!'
      }])
    except:
      response = json.dumps([{
        'Error': 'Pokemon Could Not Be Added!'
      }])
  return HttpResponse(response, content_type='text/json')








def get_pokemon(request, p_name):
  if request.method == 'GET':
    try:
      pokemon = Pokemmon.objects.get(name = p_name)
      response = json.dumps([{
        'Car': pokemon.name, 
        'HP': pokemon.hp      
      }])
    except:
      response = json.dumps([{
        'Pokemon': 'No such Pokemon exists'      
      }])     
  return HttpResponse(response, content_type = 'text/json')