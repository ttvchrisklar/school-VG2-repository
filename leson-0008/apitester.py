import requests
import random

 
pokemon_list = []

class pokemon:
    def __init__(self, name, id, type_one, type_two, abilitys, moves):
        self.name = name
        self.id = id
        self.type_one = type_one
        self.type_two = type_two
        self.abilitys = abilitys
        self.moves = moves
        pass

def get_pokemon(pokemon_id):
    ability_list = []
    move_list = []
    pokemon_data = []
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url+str(pokemon_id))
    data = response.json()
    pokemon_data.append(data["name"])
    pokemon_data.append(data["id"])
    for i in range(len(data["abilities"])):
        new_url = data["abilities"][i]["ability"]["url"]
        new_response = requests.get(new_url)
        new_data = new_response.json()
        if new_data["effect_entries"] != []:
            for l in range(len(new_data["effect_entries"])):
                if new_data["effect_entries"][l]["language"]["name"] == "en":
                    ability_list.append([data["abilities"][i]["ability"]["name"],new_data["effect_entries"][l]["short_effect"]])
                    break
    pokemon_data.append(ability_list)
    for i in range(len(data["moves"])):
        new_url = data["moves"][i]["move"]["url"]
        new_response = requests.get(new_url)
        new_data = new_response.json()
        for l in range(len(new_data["effect_entries"])):
            if new_data["effect_entries"][l]["language"]["name"] == "en":
                move_list.append([data["moves"][i]["move"]["name"],new_data["effect_entries"][0]["short_effect"], new_data["power"], new_data["pp"]])
                break
    pokemon_data.append(move_list)
    if len(data["types"]) == 2:
        pokemon_data.append([data["types"][0]["type"]["name"], data["types"][1]["type"]["name"]])
        new_pokemon = pokemon(pokemon_data[0],pokemon_data[1],pokemon_data[4][0],pokemon_data[4][1],pokemon_data[2],pokemon_data[3])
    else:
        pokemon_data.append(data["types"][0]["type"]["name"])
        new_pokemon = pokemon(pokemon_data[0],pokemon_data[1],pokemon_data[4],"null",pokemon_data[2],pokemon_data[3])
    pokemon_list.append(new_pokemon)
    print("fetching pokemon done.\n")
    main()
    
def get_random_pokemon():
    random_pokemon = random.randint(1, 1025)
    get_pokemon(random_pokemon)

def get_spesific_pokemon():
    u_input = input("give a pokedex number: ")
    if (int(u_input) >1025 or int(u_input)<1): 
        get_spesific_pokemon()
    print("fetching spesific pokemon...\n")
    get_pokemon(u_input)

def clear_list():
    global pokemon_list 
    pokemon_list = []
def print_pokemon():
    print(f'\n-------------\nname: {pokemon_list[0].name} \ntypes: {pokemon_list[0].type_one}, {pokemon_list[0].type_two} \nID: {pokemon_list[0].id}')
    print("-------------\n")
    input("when ready press enter to continu\n")
    main()    

def print_abilitys():
    print("\nAbilitys:")
    for i in range(len(pokemon_list[0].abilitys)):
        print(f' {pokemon_list[0].abilitys[i][0]}: {pokemon_list[0].abilitys[i][1]}')
    main()

def print_moves():
    print("Moves:")
    for i in range(len(pokemon_list[0].moves)):
        print(f' {pokemon_list[0].moves[i][0]}: {pokemon_list[0].moves[i][1]} Power: {pokemon_list[0].moves[i][2]} pp: {pokemon_list[0].moves[i][3]}')
    main()

def more_info():
    u_input = input("\nwhat more info do you want?\nAbilitiys: [1]\nMoves: [2]\nBack: [3]\nwrite the number in [] then press enter: ")
    match u_input:
        case "1":
            print_abilitys()
        case "2":
            print_moves()
        case "3":
            main()

def selector(input):
    match input:
        case "1":
            clear_list()
            print("fetching random pokemon...\n")
            get_random_pokemon()
        case "2":
            clear_list()
            get_spesific_pokemon()
        case "3":
            print_pokemon()
        case "4":
            more_info()
        case "5":
            quit()
        case _:
            print("\nERROR: not a suported opperation")
            main()

def main():
    u_input = input("\nselect to option you want to use bellow:\nget a random pokemon: [1]\nselect a pokemon by its pokidex number: [2]\noutput selected pokemon to see statst: [3]\nmore info in pokemon: [4]\nexit program: [5]\nwrite the number in [] then press enter: ")
    selector(u_input)
if __name__ == "__main__":
    main()