# Whorking with Arrays

players = ["charles", "martina", "michael", "florence", "eli"]
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())


print("---------------------------------------")

my_food = ["pizza", "falafel", "Carrot cake"]
friends_foods = my_food[:]

my_food.append("cannoli")
friends_foods.append("ice cream")

print("My favorite foods are :")
print(my_food)

print("\n My frined's favorite foods are:")
print(friends_foods)


print("---------------------------------------")

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


# -----------------------------------------------#
# Tuples
#   - Can only be modified if the whole thing is being
# updated 0

print("---------------------------------------")
