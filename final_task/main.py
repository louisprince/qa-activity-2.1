import sqlite3
import requests

DATABASE_NAME = 'pokemon.db'
API_URL = 'https://pokeapi.co/api/v2/pokemon/'

def connect_db() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_NAME)

def setup_db() -> None:
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon
                     (id INTEGER PRIMARY KEY,
                      name TEXT,
                      height INTEGER,
                      weight INTEGER,
                      types TEXT)''')
        connection.commit()

def create_pokemon(id: int, name: str, height: int, weight: int, types: str) -> None:
    with connect_db() as connection:
        cursor = connection.cursor()
        query = 'INSERT INTO pokemon(id, name, height, weight, types) VALUES(?,?,?,?,?)'
        cursor.execute(query, (id, name, height, weight, types))
        connection.commit()

def read_pokemon_id(id: int) -> tuple:
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pokemon WHERE id = ?', (id,))
        return cursor.fetchone()

def read_pokemon_name(name: str) -> list:
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pokemon WHERE name LIKE ?', (f'%{name}%',))
        return cursor.fetchall()

def read_all_pokemon() -> list:
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM pokemon')
        return cursor.fetchall()

def update_pokemon(id: int, new_name: str, new_height: int, new_weight: int, new_types: str) -> None:
    with connect_db() as connection:
        cursor = connection.cursor()
        query = 'UPDATE pokemon SET name = ?, height = ?, weight = ?, types = ? WHERE id = ?'
        cursor.execute(query, (new_name, new_height, new_weight, new_types, id))
        connection.commit()

def delete_pokemon(id: int) -> None:
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM pokemon WHERE id = ?', (id,))
        connection.commit()

def download_pokemon(name_or_id: str | int) -> dict | None:
    url = f'{API_URL}{name_or_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None

def print_menu() -> None:
    print("1 - View all Pokemon in Pokedex")
    print("2 - Search Pokedex using Pokedex Number")
    print("3 - Search Pokedex using Pokemon name")
    print("4 - Update Pokemon stats in Pokedex")
    print("5 - Delete Pokemon from Pokedex")
    print("6 - Download new Pokemon from Computer to Pokedex")
    print("7 - Exit Pokedex")

def main() -> None:
    setup_db()

    while True:
        print_menu()
        try:
            user_choice = int(input("Choose an option: ").strip())
        except ValueError:
            print("Option must be a number!")
            continue
        
        if user_choice == 1:
            list_of_pokemon = read_all_pokemon()
            if list_of_pokemon:
                for pokemon in list_of_pokemon:
                    print(f"Pokedex Number: {pokemon[0]}, Name: {pokemon[1]}, Height: {pokemon[2]}, Weight: {pokemon[3]}, Types: {pokemon[4]}")
            else:
                print("No Pokemon in Pokedex. Try downloading some!")
        
        elif user_choice == 2:
            try:
                id = int(input("Enter Pokedex Number: "))
                pokemon = read_pokemon_id(int(id))

                if pokemon:
                    print(f"Pokedex Number: {pokemon[0]}, Name: {pokemon[1]}, Height: {pokemon[2]}, Weight: {pokemon[3]}, Types: {pokemon[4]}")
                else:
                    print(f"No Pokemon found with Pokedex Number {id}.")
            except ValueError:
                print("Pokedex Number must contain only numbers!")
            
        elif user_choice == 3:
            name = input("Enter Pokemon name: ").strip()
            list_of_pokemon = read_pokemon_name(name)
            if list_of_pokemon:
                for pokemon in list_of_pokemon:
                    print(f"Pokedex Number: {pokemon[0]}, Name: {pokemon[1]}, Height: {pokemon[2]}, Weight: {pokemon[3]}, Types: {pokemon[4]}")
            else:
                print(f"No Pokemon found called {name}!")
        
        elif user_choice == 4:
            try:
                # Get the current values first so they can be displayed as the
                # user updates as desired
                id = int(input("Enter the Pokedex Number you would like to update: "))
                pokemon = read_pokemon_id(id)
                if not pokemon:
                    print(f"No Pokemon found with Pokedex Number {id}!")
                    continue

                name = pokemon[1]
                height = pokemon[2]
                weight = pokemon[3]
                types = pokemon[4]

                # The 'or X' at the end of these lines looks a bit weird, but
                # it will keep the current value if the user input is blank
                print('Leave a stat blank to keep current info.')
                name = input(f'Current name: "{name}". New name: ').strip() or name
                types = input(f'Current types: "{types}". New types: ').strip() or types

                try:
                    height = int(input(f'Current height: "{height}". New height: ').strip()) or height
                    weight = int(input(f'Current weight: "{weight}". New weight: ').strip()) or weight
                except ValueError:
                    print("Height and Weight must contain only numbers!")
                    continue
                
                update_pokemon(id, name, height, weight, types)
                print("Pokemon updated successfully.")
            except ValueError:
                print("Pokedex Number must contain only numbers!")
        
        elif user_choice == 5:
            try:
                id = int(input("Enter Pokedex Number you wish to delete: "))
                confirm = input(f"Are you sure you want to delete Pokedex Number {id}? y/n: ").strip().lower()
                if confirm == 'y':
                    delete_pokemon(id)
                    print("Pokemon deleted.")
                else:
                    print("Delete cancelled!")
            except ValueError:
                print("Pokedex Number must contain only numbers!")
        
        elif user_choice == 6:
            name_or_id = input("Enter Pokemon name or Pokedex number: ").strip().lower()
            data_from_api = download_pokemon(name_or_id)

            if data_from_api:
                id = data_from_api['id']
                name = data_from_api['name']
                height = data_from_api['height']
                weight = data_from_api['weight']

                """ 
                List comprehensions are a bit confusing. Instead of reading it
                in order read the "for i in data_from_api['types']" part first
                - that's the actual loop which iterates over the types array.

                Then for every element in the types array the comprehension drills
                into the json to extract the name and then adds it to the list 
                - that's the bit at the start of the comprehension i['type']['name']

                The list comprehension returns a list (who would have guessed)
                so use join to create a string out of the elements of the list
                """
                types = ', '.join([i['type']['name'] for i in data_from_api['types']])

                print(f"Downloaded Pokemon: {name}")
                print(f"Pokedex Number: {id}, Height: {height}, Weight: {weight}, Types: {types}")
                save = input(f"Save {name} to your Pokedex? y/n: ").strip().lower()
                if save == 'y':
                    existing = read_pokemon_id(id)
                    if existing:
                        print(f"{name} is already in your Pokedex!")
                    else:
                        create_pokemon(id, name, height, weight, types)
                        print(f"New Pokemon {name} saved.")
            else:
                print("Could not download Pokemon. You must enter the name of a Pokemon or a Pokedex Number.")
        
        elif user_choice == 7:
            print("Goodbye.")
            exit(0)

if __name__ == '__main__':
    main()