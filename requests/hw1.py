import requests

heroes = {}
# heroes['Dr. Strange'] = 150  # для проверки


def get_id(numb_id):
    link = 'https://superheroapi.com/api/2619421814940190/id/powerstats'
    link = link.replace('id', str(numb_id))
    response = requests.get(link)
    response.raise_for_status()
    heroes[response.json()['name']] = int(response.json()['intelligence'])
    print(response.json())
    return heroes


def cleverest(hero):
    hero = sorted(heroes, key=heroes.get, reverse=True)
    print(f'самый умный герой {hero[0]}')


get_id(332)
get_id(149)
get_id(655)
cleverest(heroes)