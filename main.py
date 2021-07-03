import requests

def most_intelegens(name_list):
  heroes_list = {}
  for name in name_list:
    url = f"https://superheroapi.com/api/2619421814940190/search/{name}"
    resp = requests.get(url)
    for hero in resp.json()['results']:
      if hero['name'] == name:
        heroes_list[name] = int(hero['powerstats']['intelligence'])
  print(f'Самый умный - {max(heroes_list, key=heroes_list.get)}')

  # intelligence_max = 0
  # name_hero = None
  # for name, number in heroes_list.items():
  #   if number > intelligence_max:
  #     intelligence_max = number
  #     name_hero = name
  # print(f'Самый умный - {name_hero}')

name_list = ['Hulk', 'Captain America', 'Thanos']
most_intelegens(name_list)
