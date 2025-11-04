# Phase 1

original_amount_str = input("Please enter the amount of the ingredient: ")
original_amount= float(original_amount_str)
original_servings_str = input("Please enter the number of the servings of the recipe: ")
original_servings = int(original_servings_str)
desired_servings_str = input("Please enter the amount of the desired servings of the recipe: ")
desired_servings = int(desired_servings_str)

# Phase 2

scaling_factor = desired_servings / original_servings
new_amount = round(original_amount * scaling_factor,1)

# Phase 3

print("---ADJUSTED RECIPE---")
print(f"The original recipe is for {original_servings} people")
print(f"To cook for {desired_servings} people, you will need {new_amount} units of your ingredient")

"""
# Bonus
# Phase 1
def check_original_amount():
    while True:
        try:
            original_amount = float(input("Please enter the amount of the ingredient: "))
            if original_amount <= 0:
                print("\033[1;31mPlease enter a valid amount.\033[m")
            else:
                return original_amount
        except ValueError:
            print("\033[1;31mPlease enter a valid amount.\033[m")

def check_original_servings():
    while True:
        try:
            original_servings = int(input("Please enter the number of the servings of the recipe: "))
            if original_servings <= 0:
                print("\033[1;31mPlease enter a valid number.\033[m")
            else:
                return original_servings
        except ValueError:
            print("\033[1;31mPlease enter a valid number.\033[m")

def check_desired_servings():
    while True:
        try:
            desired_servings = int(input("Please enter the number of the desired servings of the recipe: "))
            if desired_servings <= 0:
                print("\033[1;31mPlease enter a valid number.\033[m")
            else:
                return desired_servings
        except ValueError:
            print("\033[1;31mPlease enter a valid number.\033[m")

# Phase 2
def get_unit():
    valid_units = ["g", "kg", "ml", "l", "cup", "tbsp", "tsp"]
    unit = input("Please enter the unit of your ingredient (e.g., g,kg, ml,l,cup,tbsp,tsp): ").lower()
    if unit not in valid_units:
        print("\033[1;33mUnit not recognized, keeping it as entered.\033[m")
    return unit


def ingredients():
    ingredients = []
    ingredient_info = []
    num = int(input("How many ingredients do you want to scale? "))
    if num <= 0:
        print("\033[1;31mPlease enter a valid number.\033[m")
    else:
        for i in range(1, num + 1):
            name = input(f"Please enter the name of the ingredient n°{i}: ")
            original_amount = check_original_amount()
            original_servings = check_original_servings()
            desired_servings = check_desired_servings()
            scaling_factor = desired_servings / original_servings
            new_amount = round(original_amount * scaling_factor, 1)
            unit = get_unit()
            choice = input("Would you like to convert to larger units (e.g., g → kg)? (y/n): ").lower()
            while choice in ["y", "yes", "oui"]:
                new_amount, unit = convert_units(new_amount, unit)
                print(f"Converted amount : {new_amount} {unit}")
                choice = input("Would you like to convert again (y/n): ").lower()
                if choice not in ["y", "yes", "n", "no", "oui", "non"]:
                    print("Please enter yes or no.")
            ingredient_info = {
                "name": name,
                "original_amount": original_amount,
                "unit": unit,
                "original_servings": original_servings,
                "desired_servings": desired_servings,
                "new_amount": new_amount
            }
            ingredients.append(ingredient_info)
        return ingredients


def convert_units(amount, unit):
    conversions = {
        ("g", "kg"): amount / 1000,
        ("kg", "g"): amount * 1000,
        ("ml", "l"): amount / 1000,
        ("l", "ml"): amount * 1000,
    }
    for (from_unit, to_unit), result in conversions.items():
        if unit == from_unit:
            return result, to_unit
    return amount, unit

# Phase 3
def display_summary(ingredients_info):

    print("\033[1;33m---RECIPE SCALING SUMMARY---:\033[m")
    print("\033[90m" + "-" * 60 + "\033[m")
    print(f"{'Ingredient':<15}{'Original':>10}{'→':^5}{'New Amount':>12}{'Unit':>8}")
    print("\033[90m" + "-" * 60 + "\033[m")
    for item in ingredients_info:
        print(f"{item['name']:<15}"
            f"{item['original_amount']:>10.1f}"
            f"{'→':^5}"
            f"{item['new_amount']:>12.1f}"
            f"{item['unit']:>8}")
    print("\033[90m" + "-" * 60 + "\033[m")
    print(f"\n\033[1;36mAll ingredients scaled successfully!\033[m")


def main():

    r = "y"
    while r.lower() in ["y", "yes", "oui"]:
        print("\033[1;33mWelcome to the recipe scaler!\033[m")
        data = ingredients()
        display_summary(data)
        r = input("Would you like to scale another recipe? (y/n): ").strip().lower()
        while r not in ["y", "yes", "oui", "non", "n", "no"]:
            print("\033[1;31mPlease enter yes or no.\033[m")
            r = input("Would you like to scale another recipe? (y/n): ").strip().lower()
    print("\033[1;36mThanks for using the Recipe Scaler! Happy meal!\033[m")
if __name__ == '__main__':
    main()
"""

