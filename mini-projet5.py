# Phase 1
base_score = 1000
coins_collected_str = input("How many coins collected?")
coins_collected = int(coins_collected_str)
no_damage_answer = input("Have you finished the level without taking any damage? (y/n)")
if no_damage_answer.lower() in ["y", "yes"]:
    no_damage_bonus = True
else:
    no_damage_bonus = False

# phase 2
coin_bonus = coins_collected * 50
if no_damage_bonus:
    damage_multiplier = 2
else:
    damage_multiplier = 1

final_score = (base_score + coin_bonus) * damage_multiplier

# Phase 3

print("***LEVEL COMPLETE***")
print(f"Score: 1000 \n Coin bonus: +{coin_bonus} \n No-damage multiplier: {no_damage_bonus}")
print(f"Final score: {final_score}")

"""# Bonus
# Phase 1
base_score = 1000
def check_coins_collected():
    while True:
        try:
            coins_collected= int(input("How many coins collected?"))
            if coins_collected < 0:
                print("\033[1;31mPlease enter a valid positive number\033[m")
            else:
                return coins_collected
        except ValueError:
            print("\033[1;31mPlease enter a valid number\033[m")

def check_no_damage_bonus():
    while True:
        try:
            no_damage_answer= input("Have you finished the level without taking any damage?")
            if no_damage_answer.lower() in ["y", "yes"]:
                return True

            else:
                return False
        except ValueError:
            print("\033[1;31mPlease enter a valid answer\033[m")

# Phase 2
r = "y"
while r == "y":
    coins_collected = check_coins_collected()
    no_damage_bonus = check_no_damage_bonus()
    coin_bonus = coins_collected * 50
    if no_damage_bonus:
        damage_multiplier = 2
    else:
        damage_multiplier = 1

    final_score = (base_score + coin_bonus) * damage_multiplier

    print("\n\033[1;36m*** LEVEL SUMMARY ***\033[m")
    print(f"Base score:        {base_score}")
    print(f"Coins collected:   {coins_collected}  → Bonus: +{coin_bonus}")
    print(f"No-damage bonus:   {'Yes (x2)' if no_damage_bonus else 'No (x1)'}")
    print(f"Final score:       \033[1;32m{final_score}\033[m")
    print("-" * 35)

    r = input("Would you like to play another level? (y/n): ").strip().lower()
    while r not in ["y", "yes", "n", "no", "oui", "non"]:
        print("\033[1;31mPlease enter yes or no\033[m")
        r = input("Would you like to play another level? (y/n): ").strip().lower()

print("\033[1;36mThanks for playing! See you next time!\033[m")"""
