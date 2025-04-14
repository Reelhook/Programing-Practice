cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(len(cars))


for car in cars:
    print(car.title() + " are gay")
