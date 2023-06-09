import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # get all information as status
    print(r.status_code) # status
    print(r.text) # return from API
    print(type(r.text))
    categories =r.json() # transform to JSON as dict list
    for category in categories:
        print(category['name'])