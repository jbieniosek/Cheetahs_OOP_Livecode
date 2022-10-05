class Human:
    def __init__(self):
        self.name = ""
        self.pets = [] # list of cats and dogs
    
    def add_name(self, name):
        self.name = name
    
    def add_pets(self, pets):
        self.pets.extend(pets)