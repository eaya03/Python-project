"""# Phase 1

password = input("Please enter your password: ")
password_length = len(password)
has_digit = any(ch.isdigit() for ch in password)

#Phase 2
if password_length >= 8:
    is_long_enough = True
else:
    is_long_enough = False

if is_long_enough == True and has_digit == True:
    is_strong = True
else :
    is_strong = False

#Phase 3
print("---PASSWORD STRENGTH REPORT---")
if is_long_enough:
    print("Length of at least 8 characters: ✔")
else :
    print("Length of at least 8 characters: ✘")
if has_digit:
    print("Contains at least one digit: ✔")
else:
    print("Contains at least one digit: ✘")

if is_strong:
    print("Your password is considered strong!")
else:
    print("Your password could be improved.")"""
from datetime import datetime
import getpass

#Bonus
# Phase 1
# getpass is not functioning in the Pycharm console you can try it on VScode otherwise test it with the normal input()
def get_password():
    password = getpass.getpass("Please enter your password: ")
    password_length = len(password)
    while password.strip() == "":
        password = getpass.getpass("\033[1;31mPassword cannot be empty. Please enter your password: \033[m")
    return password
"""def get_password():
    password = input("Please enter your password: ")
    password_length = len(password)
    while password.strip() == "":
        password = input("\033[1;31mPassword cannot be empty. Please enter your password: \033[m")
    return password"""
# Phase 2
def check_length(password):
    return len(password) >= 8

def check_digit(password):
    return any(ch.isdigit() for ch in password)

def check_uppercase(password):
    return any(ch.isupper() for ch in password)

def check_lowercase(password):
    return any(ch.islower() for ch in password)

def check_special_char(password):
    return any(ch in "!@#$%^&*()" for ch in password)


# Phase 3
def calculate_score(results_dic):
    score = sum(1 for v in results_dic.values() if v)
    if score == 1 :
        strength_label = "\033[1;31mVery weak\033[m"
    elif score == 2 :
        strength_label = "\033[38;5;208mWeak\033[m"
    elif score == 3 :
        strength_label = "\033[1;33mMedium\033[m"
    elif score == 4 :
        strength_label = "\033[1;32mStrong\033[m"
    else :
        strength_label = "\033[38;5;34mVery Strong\033[m"
    return score, strength_label


# Phase 4

def give_suggestions(results_dic):
    suggestion = []
    if not results_dic["Length >= 8"]:
        suggestion.append("\033[1;33mUse at least 8 characters\033[m")
    if not results_dic["Has digit"] :
        suggestion.append("\033[1;33mTry adding digits (0-9)\033[m")
    if not results_dic["Has uppercase"] :
        suggestion.append("\033[1;33mTry adding uppercase letters (A–Z)\033[m")
    if not results_dic["Has lowercase"] :
        suggestion.append("\033[1;33mUse at least one lowercase (a-z)\033[m")
    if not results_dic["Has special char"]:
        suggestion.append("\033[1;33mAdd a special character like @ or !\033[m")

    return suggestion

# Phase 5

def display_report(results_dic, score, strength_label):
    check_mark = lambda ok: (f"\033[1;32m✔\033[m" if ok else f"\033[1;31m✘\033[m")
    print("\033[m---PASSWORD STRENGTH REPORT---\033[m")
    print(f"checked at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Length (>=8) : {check_mark(results_dic['Length >= 8'])}")
    print(f"Contains digit: {check_mark(results_dic['Has digit'])}")
    print(f"Contains uppercase: {check_mark(results_dic['Has uppercase'])}")
    print(f"Contains lowercase: {check_mark(results_dic['Has lowercase'])}")
    print(f"Contains special char: {check_mark(results_dic['Has special char'])}")
    print("------------------------------------")
    print(f"Score: {score}/5 → {strength_label}")
    suggestions = give_suggestions(results_dic)
    if suggestions:
        print("\nSuggestions:")
        for s in suggestions :
            print(f"\033[1;33m{s}\033[m")
    else:
        print("\033[1;32mNo suggestions, your password looks great\033[m")
    print()


def main():
    r = "y"
    while r.lower() in ["y", "yes", "oui"]:
        password = get_password()

        results = {
            "Length >= 8": check_length(password),
            "Has digit": check_digit(password),
            "Has uppercase": check_uppercase(password),
            "Has lowercase": check_lowercase(password),
            "Has special char": check_special_char(password),
        }

        score, label = calculate_score(results)
        display_report(results, score, label)

        if score < 4:
            r = input("Password is not strong enough. Do you want to try again? (y/n): ").strip().lower()
            if r not in ["y", "yes", "n", "no", "oui", "non"]:
                print("Please enter yes or no.")
        else:
            print("\033[1;32mGreat! Your password is strong enough!\033[m")
            r = "n"

    print(f"\033[1;36mStay safe, keep your passwords strong, and see you next time!\033[m")


main()