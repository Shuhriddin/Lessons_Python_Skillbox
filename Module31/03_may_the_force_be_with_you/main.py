# TODO здесь писать код
import requests
import json

def main():
    need_info = {}
    req_starship = requests.get('https://www.swapi.tech/api/starships/9/')

    if req_starship.status_code == 200:
        try:
            data = req_starship.json()
            print(data)
            need_info["name_ship"] = data["result"]["properties"]["name"]
            need_info["max_atmosphering_speed"] = data["result"]["properties"]["max_atmosphering_speed"]
            need_info["starship_class"] = data["result"]["properties"]["starship_class"]

            pilots_lst = []
            for i_pilot_api in data["result"]["properties"]["pilots"]:
                pilot_info = {}
                req_pilot = requests.get(i_pilot_api)
                pilot_data = req_pilot.json()
                pilot_info["name"] = pilot_data["result"]["properties"]["name"]
                pilot_info["height"] = pilot_data["result"]["properties"]["height"]
                pilot_info["mass"] = pilot_data["result"]["properties"]["mass"]

                planet_api = pilot_data["result"]["properties"]["homeworld"]
                req_planet = requests.get(planet_api)
                data_planet = req_planet.json()
                pilot_info["homeworld"] = data_planet["result"]["properties"]["name"]

                pilot_info["homeworld_link"] = pilot_data["result"]["properties"]["homeworld"]
                pilots_lst.append(pilot_info)
            need_info["pilots"] = pilots_lst
            print(need_info)

            with open('Millennium Falcon.json', 'w') as file:
                json.dump(need_info, file, indent=4)
        except json.JSONDecodeError as e:
            print("Ошибка декодирования JSON:", e)
    else:
        print("Не удалось получить данные космического корабля. Код состояния:", req_starship.status_code)


if __name__ == '__main__':
    main()
