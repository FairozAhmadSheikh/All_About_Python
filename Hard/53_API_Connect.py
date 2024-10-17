# To connect to an api we need requests library

import requests

base_url="https://pokeapi.co/api/v2/"

def get_info(name):
    url=f"{base_url}/pokemon/{name}"
    response=requests.get(url)
    
    if response.status_code==200:
        poke_data=response.json()
        return poke_data
    else:
        print(f"Failed To Retrieve data {response.status_code}")

pokemon_name=input("Enter The Name of Pokemon You Are Searching Details For : ").lower()
data=get_info(pokemon_name)
if data:
    print(f"Name : {data["name"]}")
    print(f"Height : {data["height"]}")
    print(f"Weight : {data["weight"]}")
    print(f"Type : {data["types"][0]["type"]["name"]}")