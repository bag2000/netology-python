import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
resp = requests.get(url)

all_hero = resp.json()
list_hero_for_search = ['Hulk', 'Captain America', 'Thanos']
json_list_hero_for_search = []
set_intelligence = set()

for hero in all_hero:
    if hero['name'] in list_hero_for_search:
        set_intelligence.add(hero['powerstats']['intelligence'])
        json_list_hero_for_search.append(hero)

for hero in json_list_hero_for_search:
    if hero['powerstats']['intelligence'] == max(set_intelligence):
        print(f'The smartest superhero is the {hero["name"]} with intelligence {hero["powerstats"]["intelligence"]}')
