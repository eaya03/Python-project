#phase 1
bill_total_str = input("Please enter the total amount:")
bill_total = float(bill_total_str)
tip_percent_str = input("What tip percentage would you like to leave? ")
tip_percent = int(tip_percent_str)
num_ppl_str =  input("How many people are splitting the bill? ")
num_ppl = int(num_ppl_str)
#phase 2
tip_amount = bill_total * (tip_percent / 100)
total_with_tip = bill_total + tip_amount
amount_per_person = total_with_tip / num_ppl
final_amount_per_person = round(amount_per_person, 2)
#phase 3
print("\n ---PAYMENT SUMMARY---")
print(f"total amount paid with tip is ${total_with_tip:.2f}")
print(f"Each person should pay ${final_amount_per_person:.2f}")
print(f"Based on a ${bill_total:.2f} bill with a {tip_percent:.2f}% tip shared among {num_ppl} people.")


""" Bonus
from datetime import datetime



def get_valid_amount():
    while True:
        try:
            amount = float(input("Please enter the amount:"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_tip_amount():
    while True:
        try:
            tip_amount = float(input("Please enter the tip amount:"))
            if tip_amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return tip_amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_num_ppl():
    while True:
        try:
            num_ppl = int(input("Please enter the number of people:"))
            if num_ppl <= 0:
                print("number of people must be greater than 0.")
            else:
                return num_ppl
        except ValueError:
            print("Please enter a valid number.")


def bill_breakdown():
    print("--- PAYMENT SUMMARY ---")
    print(f"Bill : ${bill_total:.2f}")
    print(f"Tip Percentage : ${tip_amount:.2f}")
    print("-----------------------")
    print(f"Total: ${total_with_tip:.2f}")
    print(f"Per Person: ${amount_per_person:.2f}")
    print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")



r = "y"
while r.lower() in ["y", "yes", "oui"]:
        bill_total = get_valid_amount()
        tip_percent = get_valid_tip_amount()
        tip_amount = bill_total * (tip_percent / 100)
        total_with_tip = bill_total + tip_amount
        amount_per_person = total_with_tip / get_valid_num_ppl()
        bill_breakdown()
        r = input("Do you want to calculate another bill? (y/n)").lower()
        if r not in ["y", "yes", "n", "no", "oui", "non"]:
            print("Please enter yes or no.")
            r = input("Do you want to calculate another bill? (y/n)").lower()
bill_breakdown()
print(f"\n thank you, Goodbye!")"""
