import sqlite3




def make_database(connection, cursor):
    #create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
        name TEXT PRIMARY KEY, 
        culture TEXT NOT NULL, 
        instructions TEXT NOT NULL,
        ingredients TEXT NOT NULL) ''')
    #save changes
    connection.commit()
    #close connection


def insert_data(recipe_list, cursor, connection):
    for recipe in recipe_list:
        cursor.execute(
            'INSERT INTO recipes (name, culture, instructions, ingredients) VALUES (?, ?, ?, ?)',
            (recipe.name(), recipe.culture(), recipe.instructions(), ", ".join(recipe.ingredients()))
        )
    connection.commit()

def search_by_name(name, connection, cursor):
    cursor.execute(
        'SELECT * FROM recipes WHERE name= ?', (name,)
    )
    return cursor.fetchall()

def search_by_ingredients(ingredient, connection, cursor):
    cursor.execute(
        'SELECT * FROM recipes WHERE instr(LOWER(ingredients), LOWER(?))>0', (ingredient,)
    )
    return cursor.fetchall()

def search_by_cultures(culture, connection, cursor):
    cursor.execute(
        'SELECT * FROM recipes WHERE culture= ?', (culture,)
    )
    return cursor.fetchall()

def sort_alphabetically(connection, cursor):
    cursor.execute(
        'SELECT * FROM recipes ORDER BY name ASC'
    )
