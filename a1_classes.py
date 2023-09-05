"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
import csv
import random
from operator import itemgetter


def main():
    """
    Main function that executes the travel tracker program.
    """
    filename = "places.csv"
    places = load_places(filename)
    display_welcome_message(places)
    while True:
        display_menu()
        choice = input(">>> ").strip().lower()
        if choice == "l":
            places = sorted(places, key=lambda x: x.priority)
            display_places(places)
        elif choice == "r":
            recommend_random_place(places)
        elif choice == "a":
            add_new_place(places)
        elif choice == "m":
            mark_visited(places)
        elif choice == "q":
            save_places("places.csv", places)
            print(f"{len(places)} places saved to {filename}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


def load_places(file_name):
    """
    Loads the list of places from a CSV file.

    Args:
    file_name (str): The name of the CSV file to load.

    Returns:
    list: A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    places = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            places.append(Place(row[0], row[1], int(row[2]), row[3] == "v"))
    return places


def save_places(file_name, places):
    """
    Saves the list of places to a CSV file.

    Args:
    file_name (str): The name of the CSV file to save.
    places (list): A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    with open(file_name, "w", newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([place.name, place.country, place.priority, "v" if place.is_visited else "n"])


def display_welcome_message(places):
    """
    Displays the welcome message for the program and the number of places loaded.
    Parameters:
    places (list): A list of places to be displayed in the message.
    """
    print("Travel Tracker 1.0 - created by Logeshwaran")
    print(f"{len(places)} places loaded from places.csv")


def display_menu():
    """
    Displays the menu of options to the user.
    """
    print("Menu:")
    print("L - List places")
    print("R - Recommend random place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def display_places(places):
    """
    Displays the list of places to the user.

    Args:
    places (list): A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    longest_name = max([len(place.name) for place in places])
    longest_country = max([len(place.country) for place in places])

    for index, place in enumerate(places, start=1):
        prefix = "*" if not place.is_visited else " "
        print(f"{prefix}{index}. {place.name.ljust(longest_name)} in {place.country.ljust(longest_country)} {place.priority}")
    unvisited_places = sum(1 for place in places if not place.is_visited)
    print(f"{len(places)} places. You still want to visit {unvisited_places} places.")


def recommend_random_place(places):
    """
    Recommends a random unvisited place from the list of places.

    Args:
    places (list): A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    unvisited = [place for place in places if not place.is_visited]
    if not unvisited:
        print("No places left to visit!")
        return
    place = random.choice(unvisited)
    print(f"Not sure where to visit next?\nHow about... {place.name} in {place.country}?")


def add_new_place(places):
    """
    Prompts the user to add a new place to the list of places.

    Args:
    places (list): A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    name = input("Name: ").strip()
    while not name:
        print("Input can not be blank")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input can not be blank")
        country = input("Country: ").strip()

    priority = int(input("Priority: "))
    places.append(Place(name, country, priority, False))
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker")


def mark_visited(places):
    """
    Marks a place as visited based on user input.

    Args:
    places (list): A list of places. Each place is represented as a list with the following elements:
    1. Name (str)
    2. Country (str)
    3. Priority (int)
    4. Visited (bool)
    """
    unvisited = [place for place in places if not place.is_visited]
    if not unvisited:
        print("No unvisited places")
        return

    display_places(places)
    index = int(input("Enter the number of a place to mark as visited\n>>> "))
    while index < 1 or index > len(places):
        print("Invalid input; enter a valid number")
        index = int(input("Enter the number of a place to mark as visited\n>>> "))

    place = places[index - 1]
    if place.is_visited:
        print(f"You have already visited {place[0]}")
        return

    place.is_visited = True
    print(f"{place.name} in {place.country} visited!")


main()

