message = input("Tell me something, and I will repeat it back to you: ")
print(message)
print("--------------------------------------")

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False
    else:
        print(message)
