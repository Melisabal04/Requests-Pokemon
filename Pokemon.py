import requests

get_url="https://pokeapi.co/api/v2/"
def take_pokemon_info(name):
    url=f"{get_url}/pokemon/{name}"
    response=requests.get(url)
    if response.status_code==200:
        pokemon_data=response.json()
        return pokemon_data
    else:
        print("Failed")

pokemon_name="leafeon"
pokemon_info=take_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name:{pokemon_info["name"]}")
    print(f"ID:{pokemon_info["id"]}")
    print(f"Height:{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")