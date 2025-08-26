from recipe_extract import *


url_link='https://www.themealdb.com/api/json/v1/1/search.php?f=a'
master_list=[]
def main():
    url_list=make_url('https://www.themealdb.com/api/json/v1/1/search.php?f=')
    for url in url_list:
        data = call_api(url)
        master_list.append(make_recipes(data))
    print(master_list)

if __name__ == "__main__":
    main()