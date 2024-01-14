import requests

def get_random_users(limit=10, categorize=None):
    response = requests.get(f'https://randomusers.me/api/?results={limit}')
    data = response.json()['results']
    
    if categorize == 'gender':
        data = sorted(data, key=lambda x: x['gender'])
        
        return data