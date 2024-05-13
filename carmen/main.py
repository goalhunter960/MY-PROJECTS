import json

def can_go(start, end, locations, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    if start == end:
        return True

    for connection in locations[start]['connections']:
        if connection not in visited and can_go(connection, end, locations, visited):
            return True

    return False


def unlock_features(features, world):
    for feature in features:
        if feature in world['locations']:
            world['locations'][feature]['locked'] = False
        elif feature in world['people']:
            world['people'][feature]['hidden'] = False
        elif feature in world['clues']:
            world['clues'][feature]['hidden'] = False


def travel_to_place(place, world):
    current_location = world['starting-location']
    locations = world['locations']

    if can_go(current_location, place, locations):
        world['starting-location'] = place
        print(f"You have travelled to {place}")
    else:
        print(f"You are unable to travel to {place}")


def talk_to_person(person, world):
    people = world['people']
    if person in people:
        info = people[person]
        if not info.get('hidden', False):
            print(info['conversation'])
            unlock_features(info.get('unlock-locations', []), world)
            unlock_features(info.get('unlock-people', []), world)
            unlock_features(info.get('unlock-clues', []), world)
        else:
            print(f"You cannot find {person} here.")
    else:
        print(f"{person} is not in this location.")


def investigate_clue(clue, world):
    clues = world['clues']
    if clue in clues:
        info = clues[clue]
        if not info.get('hidden', False):
            print(info['clue-text'])
            unlock_features(info.get('unlock-locations', []), world)
            unlock_features(info.get('unlock-people', []), world)
            unlock_features(info.get('unlock-clues', []), world)
        else:
            print("You cannot find any clue with that name.")
    else:
        print("No such clue exists.")


def game_loop(world):
    locations = world['locations']
    people = world['people']
    clues = world['clues']
    current_location = world['starting-location']

    print(f"You are at: {current_location}")

    while True:
        command = input("What would you like to do? ").strip().lower()

        if command == "display locations":
            display_locations(locations)
        elif command == "display people":
            display_people(people)
        elif command == "display clues":
            display_clues(clues)
        elif command.startswith("go to ") or command.startswith("travel to "):
            destination = command.split(maxsplit=2)[-1]
            travel_to_place(destination, world)
        elif command.startswith("talk to "):
            person = command.split(maxsplit=2)[-1]
            talk_to_person(person, world)
        elif command.startswith("investigate "):
            clue = command.split(maxsplit=1)[-1]
            investigate_clue(clue, world)
        elif command == "quit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")
def display_locations(locations):
    print("Locations:")
    for location in locations:
        print("-", location)

def display_people(people):
    print("People:")
    for person, info in people.items():
        if not info.get('hidden', False):
            print("-", person)

def display_clues(clues):
    print("Clues:")
    for clue, info in clues.items():
        if not info.get('hidden', False):
            print("-", clue)

def game_loop(world):
    locations = world['locations']
    people = world['people']
    clues = world['clues']
    current_location = world['starting-location']

    print(f"You are at: {current_location}")

    while True:
        command = input("What would you like to do? ").strip().lower()

        if command == "display locations":
            display_locations(locations)
        elif command == "display people":
            display_people(people)
        elif command == "display clues":
            display_clues(clues)
        elif command.startswith("go to ") or command.startswith("travel to "):
            # Implement travel functionality
            pass
        elif command.startswith("talk to "):
            # Implement talk to person functionality
            pass
        elif command.startswith("investigate "):
            # Implement investigate clue functionality
            pass
        elif command == "quit":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

def main():
    file_name = input("Enter the name of the game file: ")
    game_data = load_game_data(file_name)
    world = build_world(game_data['locations'], game_data['people'], game_data['clues'])
    print("Game data loaded successfully!")

    game_loop(world)

if __name__ == "__main__":
    main()