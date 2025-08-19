from recipe_extract import call_api, print_recipes


url='https://www.themealdb.com/api/json/v1/1/search.php?f=a'

def main():
    data=call_api(url)
    print_recipes(data)

main()