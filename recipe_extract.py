import requests
import json

class Recipe:

    def __init__(self, name, culture, instructions, ingredients):
        self._name=name
        self._culture=culture
        self._instructions=instructions
        self._ingredients= ingredients

    def name(self):
        return self._name

    def culture(self):
        return self._culture

    def instructions(self):
        return self._instructions

    def ingredients(self):
        return self._ingredients

    def __str__(self):
        return (
            f'Name: {self._name}\n'
            f'Culture: {self._culture}\n'
            f'Instructions: {self._instructions}\n'
            f'Ingredients: {', '.join(self._ingredients)}'
        )
def call_api(link):
    response=requests.get(link)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print('ERROR AHHH')
def make_recipes(recipes):
    recipe_list=[]
    if recipes['meals'] is None:
        return recipe_list
    for meal in recipes['meals']:
        ingredients_list=extract_ingredients_and_measurements(meal)
        r=Recipe(extract_name(meal), extract_culture(meal), extract_instructions(meal), ingredients_list)
        recipe_list.append(r)
    return recipe_list


def extract_name(recipe_dict):
    return recipe_dict['strMeal']

def extract_culture(recipe_dict):
    return recipe_dict['strArea']

def extract_instructions(recipe_dict):
    return recipe_dict['strInstructions']


def extract_ingredients_and_measurements(recipe_dict):
    merged_list = []
    for i in range(1, 21):
        ingredient = recipe_dict.get(f"strIngredient{i}")
        measurement = recipe_dict.get(f"strMeasure{i}")

        if ingredient and ingredient.strip():
            if measurement and measurement.strip():
                merged_list.append(f"{measurement.strip()} {ingredient.strip()}")
            else:
                merged_list.append(ingredient.strip())
    return merged_list

def make_url(base):
    count=0
    url_list=[]
    alphabet='abcdefghijklmnopqrstuvwxyz'
    length=len(alphabet)
    while count<length:
        url_list.append(base+alphabet[count])
        count+=1
    return url_list

