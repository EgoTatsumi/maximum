import requests
from pprint import pprint


def check(url):
    diameters = []
    for i in range(1, 11):
        response = requests.get(f'{url}/{i}').json()
        diameters.append({response.get('name'): response.get('diameter')})
    pprint(diameters)



url = 'https://swapi.dev/api/'
response = requests.get(url).json()
# pprint(response)
people_api = response.get('people')
planets_api = response.get('planets')
# print(people_api)
check(planets_api)