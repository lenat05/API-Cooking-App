import sqlite3

def make_database():
    #connect to database
    connection= sqlite3.connect("recipes.db")
    #create cursor
    cursor=connection.cursor()
    #create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
        name TEXT PRIMARY KEY, 
        culture TEXT NOT NULL, 
        instructions TEXT NOT NULL,
        ingredients TEXT NOT NULL) ''')
    #save changes
    connection.commit()
    #close connection
    connection.close()
