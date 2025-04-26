def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""

    print(f"\nI have {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

    if animal_type == "cat":
        print("I should never have gotten a cat")


describe_pet("Fucker", "cat")
describe_pet(pet_name="riley")
describe_pet("Gunner")
# describe_pet("lab shepard mix", "Gunner")
# describe_pet("Huskey", "riley")
