import random
import pyperclip
import csv

# Character Sets
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};':\"\\|,.<>/?`~"

# Generates a strong, random password
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols):
    all_chars = ""
    if use_lowercase:
        all_chars += lowercase
    if use_uppercase:
        all_chars += uppercase
    if use_numbers:
        all_chars += numbers
    if use_symbols:
        all_chars += symbols

    guaranteed_chars = []
    if use_lowercase:
        guaranteed_chars.append(random.choice(lowercase))
    if use_uppercase:
        guaranteed_chars.append(random.choice(uppercase))
    if use_numbers:
        guaranteed_chars.append(random.choice(numbers))
    if use_symbols:
        guaranteed_chars.append(random.choice(symbols))

    random_chars = [random.choice(all_chars) for _ in range(length - len(guaranteed_chars))]
    password = guaranteed_chars + random_chars
    random.shuffle(password)
    return "".join(password)

# Main program loop
def main():
    while True:
        try:
            length = int(input("Enter desired password length (at least 8 recommended): "))
            if length < 8:
                print("Password should be at least 8 characters for better security.")
                continue 

            use_lowercase = False  # Set defaults in case of invalid input
            use_uppercase = False
            use_numbers = False
            use_symbols = False

            def get_user_choice(prompt):
                while True:
                    try:
                        choice = input(prompt).lower()
                        if choice in ['y', 'n']:  # Check for valid input
                            return choice == 'y'
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")
                    except ValueError:  # Catch potential errors from input()
                        print("Invalid input. Please enter 'y' or 'n'.")

            use_lowercase = get_user_choice("Include lowercase letters? (y/n): ")
            use_uppercase = get_user_choice("Include uppercase letters? (y/n): ")
            use_numbers = get_user_choice("Include numbers? (y/n): ")
            use_symbols = get_user_choice("Include symbols? (y/n): ")

            password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_symbols)
            print("Generated Password:", password)

            copy_to_clipboard = input("Copy password to clipboard? (y/n): ").lower() == 'y'
            if copy_to_clipboard:
                pyperclip.copy(password)
                print("Password copied to clipboard!")

            save_password = input("Save this password? (y/n): ").lower() == 'y'
            read_passwords = False
            if save_password:
                # ... (Save password code - same as before)
                read_passwords = input("Read saved passwords? (y/n): ").lower() == 'y'
            if read_passwords:
                with open("saved_passwords.csv", 'r', newline='') as f:
                    reader = csv.reader(f)
                    for row in reader:
                        print(f"Username: {row[0]}, Platform: {row[1]}")

            generate_more = input("Generate another password? (y/n): ").lower()
            if generate_more != 'y':
                break 

        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
