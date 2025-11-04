#Phase 1
distance_miles_str = input("Please enter the distance in miles:")
distance_miles = float(distance_miles_str)
efficiency_str = input("Please enter the efficiency of the vehicle in miles per gallon: ")
efficiency = float(efficiency_str)
price_per_gallon = input("Please enter the price of one gallon of gas: ")
price_per_gallon = float(price_per_gallon)

#Phase 2
gallons_needed = distance_miles / efficiency
total_cost = round(gallons_needed * price_per_gallon,2)

#Phase 3
print("--- ESTIMATED FUEL BUDGET ---")
print(f"The total trip distance is {distance_miles} miles.")
print(f"The estimate fuel cost for this trip will be ${total_cost}.")
print(f"The total gallons of gas needed will be {gallons_needed:.2f}.")


""" # Bonus

from datetime import datetime

# Phase 1
def get_validate_distance():
    while True:
        try:
            distance_miles = float(input("Please enter the distance in miles: "))
            if distance_miles <= 0:
                print("\033[1;31mPlease enter a valid distance.\033[m")
            else:
                return distance_miles
        except ValueError:
            print("\033[1;31mPlease enter a valid distance.\033[m")

def get_validate_efficiency():
    while True:
        try:
            efficiency = float(input("Please enter the efficiency of the vehicle in miles per gallon: "))
            if efficiency <= 0:
                print("\033[1;31mPlease enter a valid efficiency.\033[m")
            else :
                return efficiency
        except ValueError:
            print("\033[1;31mPlease enter a valid efficiency.\033[m")

def get_validate_price_per_gallon():
    while True:
        try:
            price_gallon = float(input("Please enter the price of one gallon of gas: "))
            if price_gallon <= 0:
                print("\033[1;31mPlease enter a valid price.\033[m")
            else:
                return price_gallon
        except ValueError:
            print("\033[1;31mPlease enter a valid price.\033[m")

def get_validate_budget():
    while True:
        try:
            budget = float(input("Please enter your budget: "))
            if budget <= 0:
                print("\033[1;31mPlease enter a valid budget.\033[m")
            else :
                return budget
        except ValueError:
            print("\033[1;31mPlease enter a valid budget.\033[m")

# Phase 2
distance_miles = get_validate_distance()
efficiency = get_validate_efficiency()
price_per_gallon = get_validate_price_per_gallon()

gallons_needed = distance_miles / efficiency
total_cost = round(gallons_needed * price_per_gallon,2)

budget = get_validate_budget()
def calcul():
    diff = round(budget - total_cost,2)
    if diff >= 0:
        print(f"\033[1;32mYou're within your budget by ${diff}\033[m")
    else :
        print(f"\033[1;31mYou'll exceed your budget by ${abs(diff)}\033[m")

# Phase 3
def summary_breakdown():
    print("\033[1;33m---ESTIMATED FUEL BUDGET ---\033[m")
    print(f"Distance: {distance_miles:.2f} miles")
    print(f"Efficiency: {efficiency:.2f} mpg")
    print(f"Gas price: ${price_per_gallon:.2f}")
    print(f"Gallons needed: {gallons_needed:.2f}")
    print(f"Total cost: ${total_cost:.2f}")
    print(f"Budget: ${budget:.2f}")
    calcul()
    print(f"Date : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

def checklist():
    tasks = []
    print("\033[1;33m---TRIP CHECKLIST---\033[m")
    print("\033[3mYou can now create your own checklist before the trip!\033[0m")
    num = int(input("How many tasks do you want to add? "))
    if num <= 0:
        print("\033[1;31mPlease enter a valid number.\033[m")
    else :
        for i in range(1,num+1):
            task = input(f"Enter task #{i}:")
            tasks.append(task)

    done = 0
    not_done = 0
    for t in tasks:
        r = input(f"Did you complete this task {t}? (y/n): ")
        if r.lower() in ["y", "yes", "oui"]:
            done += 1
            print(f"\033[1;32m{t}\033[m")
        elif r.lower() in ["n", "no", "non"]:
            not_done += 1
            print(f"\033[1;31m{t}\033[m")
        else :
            print(f"\033[1;31mEnter a valid answer\033[m")

    if done == len(tasks):
        print(f"\033[1;32mYou're ready to go\033[m")
    elif not_done == len(tasks):
        print(f"\033[1;31mYou're not ready yet\033[m")
    else:
        print(f"\033[1;33mYou completed only {done} tasks, you still have {not_done} task uncompleted\033[m")


summary_breakdown()
checklist()
print(f"\033[1;36mThank you for using Trip Fuel Calculator! Have a safe journey\033[m")"""