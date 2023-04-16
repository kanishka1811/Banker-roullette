import random
names = input("Give me everybody's names, separated by a comma.\n")

list = names.split(", ")

random_index = random.randint(0, len(list)-1)

random_name = list[random_index]

print(f"{random_name} is going to buy the meal today!")