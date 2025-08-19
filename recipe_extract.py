import requests
import json

class Recipe:

    def __init__(self, name, culture, instructions):
        self._name=''
        self._culture=''
        self._instructions=''

def call_api(link):
    response=requests.get(link)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print('ERROR AHHH')
def print_recipes(recipes):
    for element in recipes['meals']:
        r=Recipe(extract_name(element), extract_culture(element), extract_instructions(element))

def extract_name(recipe_dict):
    print(recipe_dict['strMeal'][:-1])
    return recipe_dict['strMeal']

def extract_culture(recipe_dict):
    return recipe_dict['strArea']

def extract_instructions(recipe_dict):
    return recipe_dict['strInstructions']

