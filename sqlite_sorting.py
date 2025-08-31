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

def search_by_name(name, cursor, connection):
    cursor.execute(
        'SELECT * FROM recipes WHERE name= ?, (name)'
    )
    return cursor.fetchall()

