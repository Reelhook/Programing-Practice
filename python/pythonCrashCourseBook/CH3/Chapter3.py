import typing
from typing import Iterable


bicycles = ["trek", "cannondale", "redline", "specialized", "Jesus", "IDK"]
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print("Hello World")
for x in bicycles:
    print(x)
# --------------------------------------------------#
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


pizza = ["perperoni", "Cheese", "supreme"]

for pizzaKind in pizza:
    print("Damn that " + pizzaKind.lower() + " was good")
    pass

for value in iterable:
    pass
