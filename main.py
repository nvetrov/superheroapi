from pprint import pprint
import requests


def get_data_hero(search_hero):
    hero_dict = dict()
    for name_hero in search_hero:
        url = f' https://superheroapi.com/api/'
        token = "2619421814940190/"
        full_url = url + token + "/search/" + name_hero
        r = requests.get(full_url)
        # print(r.url)
        # print(r.status_code)
        hero_json = r.json()
        hero_lst = []
        d = {}
        try:
            for current_hero in hero_json['results']:
                if current_hero['name'] == name_hero:
                    d['id'] = current_hero['id']
                    d['name'] = current_hero['name']
                    d['intelligence'] = current_hero['powerstats']['intelligence']
                    hero_lst.append(d)
                    hero_dict[name_hero] = hero_lst
        except KeyError as e:
            print(f' Персонажа  {name_hero} нет')

    return hero_dict


if __name__ == '__main__':
    name = ['Hulk', 'Captain America', 'Thanos']
    hero_result = get_data_hero(name)
    max = 0
    for  v in hero_result.values():
        if max > int(v[0]['intelligence']):
            continue
        else:
            max = int(v[0]['intelligence'])

    for k, v in hero_result.items():
        if max == int(v[0]['intelligence']):
            print(k, max)
            break

