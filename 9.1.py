import requests

url_heroes = 'https://akabab.github.io/superhero-api/api/all.json'
heroes_name_list = ["Hulk", "Captain America", "Thanos"]


def heroes_check(url, heroes: list):
    response = requests.get(url).json()
    best_hero = None
    best_intelligence = 0
    for item in response:
        for hero_name in heroes_name_list:
            if hero_name == item['name'] and best_intelligence < item['powerstats']['intelligence']:
                best_hero = item['name']
                print(best_hero)
    print(f'{best_hero} самый умный супергерой.')


if __name__ == '__main__':
    heroes_check(url_heroes, heroes_name_list)
