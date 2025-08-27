from recipe_extract import *
from sqlite_sorting import *
import sqlite3

url_link='https://www.themealdb.com/api/json/v1/1/search.php?f=a'

def main():
    master_list = []
    # connect to database
    conn = sqlite3.connect("recipes.db")
    # create cursor
    curs = conn.cursor()
    url_list=make_url('https://www.themealdb.com/api/json/v1/1/search.php?f=')
    for url in url_list:
        data = call_api(url)
        master_list.extend(make_recipes(data))
    insert_data(master_list, curs, conn)
    conn.close()



if __name__ == "__main__":
    main()