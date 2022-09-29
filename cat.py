class Cat:
    def __init__(self, cat_name, attitude):
        self.name = cat_name
        self.feeling = attitude
        self.hat = None

    def purr(self):
        print("Purr")

    def change_attitude(self, new_hat, new_attitude = "cheerful"):
        self.feeling = new_attitude
        self.hat = new_hat
        print("new hat: ", new_hat)
        print("new attitude", new_attitude)
    
    def get_attitude(self):
        print(self.feeling)