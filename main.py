from dog import Dog
from cat import Cat
from corgi import Corgi
from persian import Persian
from human import Human

petey = Persian("Petey", "sleepy")
coral = Corgi("Coral", 1, "brown", [petey], "small")
pumpkin = Corgi("Pumpkin", 10, "black", [petey], "large")

print(f"Coral has a cat named {coral.num_pets[0].name}")
print(coral.human)
print(pumpkin.human)

coral.human.add_name("Ada")
pumpkin.human.add_name("Nancy")
print(coral.human.name)
print(pumpkin.human.name)

print(f"{coral.human.name} has {coral.human.pets[0].name}")
print(f"{pumpkin.human.name} has {pumpkin.human.pets[0].name}")

# moana = Human("Moana", [petey, coral])

# for pet in moana.pets:
#     print(pet.name)
#     if isinstance(pet, Persian):
#         pet.brush()
#     else:
#         pet.about()



############# OOP Lesson code below ################

# alfosina = Persian("Alfosina", "grumpy")
# print(vars(alfosina))
# alfosina.get_attitude()
# alfosina.brush()

# cat1 = Cat("Bailey", "indifferent")
# cat1.get_attitude()
# # cat1.brush() <-- will cause error




# pet_list = list()
# print(pet_list)

# cheddar = Corgi("Cheddar", 4, "sable", "small")

# pet_list.append(cheddar)
# print(pet_list)

# print(cheddar)
# print(vars(cheddar))

# cheddar.about()

# rufus = Corgi("Rufus", 4, "sable", "huge")
# rufus.about()

'''

cat1 = Cat("Inu", "happy")
cat1.purr()
cat1.get_attitude()
#print("weirdness starts here:")
cat1.change_attitude("top_hat")#"grumpy")
cat1.get_attitude()
pet_list.append(cat1)

dog1 = Dog("River", "mutt", 3, "brown")

dog1.about()
for i in range(5):
    dog1.pet_dog()
pet_list.append(dog1)
dog2 = Dog("Titus", "mutt", 15, "white, orange and brown")
dog2.pet_dog()
pet_list.append(dog2)

print(pet_list)
'''