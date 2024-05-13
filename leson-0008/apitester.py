import requests
import random

pokemon_list = []

class pokemon:
    def __init__(self, name, id, type_one, type_two):
        self.name = name
        self.id = id
        self.type_one = type_one
        self.type_two = type_two
        pass

def get_pokemon(pokemon_id):
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url+str(pokemon_id))
    data = response.json()
    pokemon_data = []
    pokemon_data.append(data["name"])
    pokemon_data.append(data["id"])
    if len(data["types"]) == 2:
        pokemon_data.append([data["types"][0]["type"]["name"], data["types"][1]["type"]["name"]])
        new_pokemon = pokemon(pokemon_data[0],pokemon_data[1],pokemon_data[2][0],pokemon_data[2][1])
    else:
        pokemon_data.append(data["types"][0]["type"]["name"])
        new_pokemon = pokemon(pokemon_data[0],pokemon_data[1],pokemon_data[2],"null")
    pokemon_list.append(new_pokemon)
    main()
    
def get_random_pokemon():
    random_pokemon = random.randint(1, 1025)
    get_pokemon(random_pokemon)

def get_spesific_pokemon():
    u_input = input("give a pokedex number: ")
    if (int(u_input) >1025 or int(u_input)<1): 
        get_spesific_pokemon()
    get_pokemon(u_input)

def clear_list():
    global pokemon_list 
    pokemon_list = []
def print_pokemon():
    print("\n-------------")
    print(f' name: {pokemon_list[0].name} \n types: {pokemon_list[0].type_one}, {pokemon_list[0].type_two} \n ID: {pokemon_list[0].id}')
    print("-------------")
    main()

def selector(input):
    match input:
        case "1":
            clear_list()
            get_random_pokemon()
        case "2":
            clear_list()
            get_spesific_pokemon()
        case "3":
            print_pokemon()
        case "4":
            quit()
        case _:
            print("\nERROR: not a suported opperation")
            main()

def main():
    u_input = input("\nselect what acsion to do: \nget a random pokemon: 1 \nselect a pokemon: 2 \nprint your selectded pokemon: 3 \nexit: 4 \nselect by writing 1-4: ")
    selector(u_input)            

if __name__ == "__main__":
    main()