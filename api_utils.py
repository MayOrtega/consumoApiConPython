# api_utils.py
import requests

def get_random_users(limit=10, categorize=None):
    response = requests.get(f'https://randomuser.me/api/?results={limit}')
    data = response.json()['results']

    if categorize == 'gender':
        data = sorted(data, key=lambda x: x['gender'])

    return data

def get_user_with_favorite_drink():
    response_users = requests.get('https://randomuser.me/api/?results=10')
    users_data = response_users.json()['results']

    response_drinks = requests.get('https://www.thecocktaildb.com/api/json/v1/1/random.php')
    drink_data = response_drinks.json()['drinks'][0]

    result = []
    for user in users_data:
        user_with_drink = {
            'name': user['name']['first'],
            'last_name': user['name']['last'],
            'email': user['email'],
            'nationality': user['nat'],
            'favorite_drink': drink_data['strDrink']
        }
        result.append(user_with_drink)

    return result
