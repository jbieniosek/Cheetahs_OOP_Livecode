from dog import Dog
from cat import Cat

pet_list = list()
print(pet_list)

cat1 = Cat("Inu", "happy")
cat1.purr()
cat1.get_attitude()
#print("weirdness starts here:")
cat1.change_attitude("top_hat")#"grumpy")
cat1.get_attitude()
pet_list.append(cat1)
'''
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