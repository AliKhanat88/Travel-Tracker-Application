from place import Place
from functools import cmp_to_key

def compare_name(a, b):
    if a.name > b.name:
        return 1
    elif a.name == b.name:
        if a.priority > b.priority:
            return 1
        else:
            return -1
    else:
        return -1
    
def compare_country(a, b):
    if a.country > b.country:
        return 1
    elif a.country == b.country:
        if a.priority > b.priority:
            return 1
        else:
            return -1
    else:
        return -1
    
def compare_visited(a, b):
    if a.is_visited == b.is_visited:
        if a.priority > b.priority:
            return 1
        else:
            return -1
    elif a.is_visited == True:
        return 1
    else:
        return -1
    


# Create your PlaceCollection class in this file


class PlaceCollection:
    def __init__(self):
        self.places = []

    def add_place(self, place):
        self.places.append(place)

    def load_places(self, filename=""):
        self.places = []
        if filename == "":
            return
        file = open(filename, "r")
        line = file.readline().strip()
        while line != "":
            name, country, priority, visited = line.strip().split(",")
            if visited == "v":
                self.add_place(Place(name, country, int(priority), True))
            else:
                self.add_place(Place(name, country, int(priority), False))
            line = file.readline().strip()
        file.close()
    
    def save_places(self, filename=""):
        if filename == "":
            return
        file = open(filename, "w")
        for place in self.places:
            temp = "v" if place.is_visited else "r"
            file.write(f"{place.name},{place.country},{place.priority},{temp}\n")
        file.close()

    def get_number_of_unvisited(self):
        count = 0
        for place in self.places:
            if place.is_visited == False:
                count += 1
        return count
    
    def sort(self, att):
        if att == "name":
            self.places = sorted(self.places, key=cmp_to_key(compare_name))
        elif att == "country":
            self.places = sorted(self.places, key=cmp_to_key(compare_country))
        elif att == "visited":
            self.places = sorted(self.places, key=cmp_to_key(compare_visited))
        elif att == "priority":
            self.places = sorted(self.places, key=lambda x: x.priority)
    
    def __str__(self):
        r = ""
        for place in self.places:
            r += place.__str__() + "\n"
        return r

