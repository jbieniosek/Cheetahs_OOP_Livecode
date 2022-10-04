from dog import Dog

class Corgi(Dog):

    def __init__(self, name, age, color, size):
        super().__init__(name, "Corgi", age, color)
        self.size = size
    
    def about(self):
        super().about()
        print(f"{self.name} is a corgi.")
        print(f"{self.name} is {self.color} and {self.size}")
    