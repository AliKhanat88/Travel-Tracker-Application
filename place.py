"""..."""


# Create your Place class in this file


class Place:
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        if self.is_visited == True:
            return f"{self.name} in {self.country}, priority {self.priority} (visited)"
        else:
            return f"{self.name} in {self.country}, priority {self.priority}"
    
    def mark_visited(self):
        self.is_visited = True
        
    def mark_unvisited(self):
        self.is_visited = False

    def isImp(self):
        if self.priority <= 2:
            return True
        return False
    
