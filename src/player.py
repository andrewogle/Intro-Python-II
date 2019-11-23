# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.name = ''
        self.location = location
        self.game_over = False
   