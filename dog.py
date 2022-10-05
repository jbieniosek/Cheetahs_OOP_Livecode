from human import Human

class Dog:
    def __init__(self, name, breed, age, color, num_pets):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.num_pets = num_pets
        self.human = Human()
        self.human.add_pets([self])
    
    def about(self):
        #self.name = "Spot"
        print(f"This is a dog named {self.name}")
        print(f"{self.name} is {self.age} years old")
    
    def pet_dog(self):
        self.num_pets += 1
        print(f"{self.name} has been petted {self.num_pets} times")
        if self.num_pets % 5 == 0:
            self.bark()
    
    def bark(self):
        print("woof")
