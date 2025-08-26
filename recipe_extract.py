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

def call_api(link):
    response=requests.get(link)
    if response.status_code==200:
        data=response.json()
        return data
    else:
        print('ERROR AHHH')
def make_recipes(recipes):
    recipe_list=[]
    for meal in recipes['meals']:
        ingredients_list=merge_measurements_ingredients(extract_ingredients(meal), extract_measurements(meal))
        r=Recipe(extract_name(meal), extract_culture(meal), extract_instructions(meal), ingredients_list)
        recipe_list.append(r)
    return recipe_list


def extract_name(recipe_dict):
    return recipe_dict['strMeal']

def extract_culture(recipe_dict):
    return recipe_dict['strArea']

def extract_instructions(recipe_dict):
    return recipe_dict['strInstructions']

def extract_ingredients(recipe_dict):
    ingredients_list=[]
    for key in recipe_dict.keys():
        if key.startswith('strIngredient') and recipe_dict[key]!=''and recipe_dict[key] and recipe_dict[key]!=' ':
            ingredients_list.append(recipe_dict[key])
    print(len(ingredients_list))
    return ingredients_list

def extract_measurements(recipe_dict):
    measurements_list=[]
    for key in recipe_dict.keys():
        if key.startswith('strMeasure') and recipe_dict[key]!='' and recipe_dict[key] and recipe_dict[key]!=' ':
            measurements_list.append(recipe_dict[key])
    print(len(measurements_list))
    return measurements_list

def merge_measurements_ingredients(ingredients_list, measurements_list):
    merged_list=[]
    count=0
    #add a check for if the lengths arent the same later
    list_lengths=len(ingredients_list)
    while count<list_lengths:
        merged_list.append(measurements_list[count]+ ' '+ ingredients_list[count])
        #problem: it doesnt add inches. or certain measurements and im sad
        count+=1
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