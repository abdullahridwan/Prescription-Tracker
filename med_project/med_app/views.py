from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

import json
from med_app.models import Pokemon


def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


@csrf_exempt
def add_pokemon(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        p_name = payload['name']
        p_hp = payload['hp']

        num_of_p = Pokemon.objects.filter(name=p_name).count()
        if num_of_p == 0:
            try:
                pokemon = Pokemon(name=p_name, hp=p_hp)
                pokemon.save()
                response = json.dumps([{
                    'Success': 'Pokemon Added Sucessfully!'
                }])
            except Exception as e:
                response = json.dumps([{
                    'Error': 'Pokemon Could Not Be Added!',

                }])
            return HttpResponse(response, content_type='text/json')
        else:
            response = json.dumps([{
                'Error': 'Pokemon Already Exists!',

            }])
            return HttpResponse(response, content_type='text/json')


# return a specific pokemons json
@csrf_exempt
def pokemon(request, p_name):
    if request.method == 'GET':
        try:
            pokemon = Pokemon.objects.get(name=p_name)
            response = json.dumps([{
                "name": pokemon.name,
                'hp': pokemon.hp
            }])
        except:
            response = json.dumps([{
                "Error": "Could not get Pokemon"
            }])
        return HttpResponse(response, content_type='text/json')
    elif request.method == "DELETE":
        count = Pokemon.objects.filter(name=p_name).count()
        try:
            if count == 0:
                response = json.dumps([{"Error": "Pokemon does not existed!"}])
            else:
                Pokemon.objects.filter(name=p_name).delete()
                response = json.dumps(
                    [{"Success": p_name + " pokemon deleted!"}])
        except:
            response = json.dumps([{
                "Error": "Pokemon Could not be Deleted!"
            }])
        return HttpResponse(response, content_type="content/type")

# returns list of all pokemons


def get_all_pokemon(request):
    if request.method == 'GET':
        Pokemon_json = serializers.serialize("json", Pokemon.objects.all())
    return HttpResponse(Pokemon_json, content_type='text/json')
