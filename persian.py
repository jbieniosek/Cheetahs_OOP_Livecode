from cat import Cat

class Persian(Cat):

    def __init__(self, cat_name, attitude):
        super().__init__(cat_name, attitude)
        self.fur = "long"
    
    def brush(self):
        print("giant furball")