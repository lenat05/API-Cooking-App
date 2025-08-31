from recipe_extract import *
from sqlite_sorting import *
import sqlite3
import os


def create_database(conn, curs):
    master_list = []
    url_list = make_url('https://www.themealdb.com/api/json/v1/1/search.php?f=')
    for url in url_list:
        data = call_api(url)
        master_list.extend(make_recipes(data))
    make_database(conn, curs)
    insert_data(master_list, curs, conn)

def delete_database():
    db_file = "recipes.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"{db_file} deleted.")
    else:
        print("Database file not found.")

def main():
    if not os.path.exists("recipes.db"):
        # connect to database
        conn = sqlite3.connect("recipes.db")
        # create cursor
        curs = conn.cursor()
        create_database(conn, curs)
        conn.close()
    else:
        print('yay database')

if __name__ == "__main__":
    main()