# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, discription, item = None):
        self.discription = discription
        self.name = name
        self.item = []
        self.n_to = "wall"
        self.s_to = "wall"
        self.e_to = "wall"
        self.w_to = "wall"

    def __str__(self):
        return f'your current location is {self.name}'