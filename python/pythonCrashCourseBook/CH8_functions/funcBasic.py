def explain():
    """Explains what the user input is suppose to be."""
    print("Input the user name")


def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


explain()
greet_user(input("Name="))
