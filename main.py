import os
import random
import string
import re
import time
import sys
import math

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_text(text, delay=0.03): # increase the delay for slower effect :)
    for i, char in enumerate(text):
        r = int(math.sin(0.3 * i + 0) * 127 + 128)
        g = int(math.sin(0.3 * i + 2) * 127 + 128)
        b = int(math.sin(0.3 * i + 4) * 127 + 128)
        sys.stdout.write(f"\033[38;2;{r};{g};{b}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def evaluate_password_strength(password):
    min_length = 8
    max_length = 50
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    length_ok = min_length <= len(password) <= max_length

    if not length_ok:
        return "Weak/Out of character limit: Password must be between 8 and 50 characters."
    if has_upper and has_lower and has_digit and has_special:
        return "Strong: Your password is strong."
    return "Moderate: Consider adding more complexity (uppercase, lowercase, digits, special characters)."

def generate_strong_password(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    all_characters = lower + upper + digits + special
    password += random.choices(all_characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

def main():
    while True:
        clear_screen()
        rainbow_text("================================================================", 0.01) # Adjust delay for effect
        rainbow_text("          PASSWORD STRENGTH CHECKER AND GENERATOR", 0.01)
        rainbow_text("           Author: Shane Green (ShaneYLad)", 0.01)
        rainbow_text("================================================================\n", 0.01)
        time.sleep(0.5)

        print("Select an option:")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit\n")

        choice = input("Enter your choice (1, 2, or 3): ")

        match choice:
            case '1':
                password = input("\nEnter your password: ")
                result = evaluate_password_strength(password)
                print(result, "\n")

            case '2':
                try:
                    length = int(input("\nEnter desired password length (min 8): "))
                    password = generate_strong_password(length)
                    if password:
                        print("Generated Password:", password, "\n")
                except ValueError:
                    print("\nPlease enter a valid number.")
                    time.sleep(2)

            case '3':
                print("\nExiting the program. Stay safe!")
                break

            case _:
                print("Invalid choice. Please select 1, 2, or 3.")

        back = input("\nGo back to main menu? (y/n): ").lower()
        if not back.startswith('y'):
            print("Exiting the program. Stay safe!")
            break

if __name__ == "__main__":
    main()