import random

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "!@#$%&*^|()_+"

def get_available_chars(include_digits, include_special):
    available_chars = alpha
    if include_digits:
        available_chars += num
    if include_special:
        available_chars += special
    return available_chars

def generate_password(length = 16, mixed_case = False, 
                      include_digits = False, include_special = False):
    password = []
    available_chars = get_available_chars(include_digits, include_special)
    
    for i in range(length):
        character = random.choice(available_chars)
        
        if mixed_case and character.isalpha():
            change_to_upper = random.randint(0, 1)
            if change_to_upper:
                character = character.upper()
                
        password.append(character)
    return ''.join(password)

def interact_main_menu():
    while True:
        print('\n-- Password generator --')
        print('Choose option:')
        print('1: generate password')
        print('2: exit the program')
        user_choice = input('Your choice: ')
        if user_choice == '1':
            interact_password_type()
        elif user_choice == '2':
            print('Bye!')
            break
        else:
            print('Please enter a correct value')

def interact_password_type():
    length = int(input('Provide password length: '))
    include_upper = input('Use uppercase letters? (y/n): ').lower().strip() == 'y'
    include_digits = input('Use digits? (y/n): ').lower().strip() == 'y'
    include_special = input('Use special characters? (y/n): ').lower().strip() == 'y'
    print('\nGenerated password:', generate_password(length, include_upper, include_digits, include_special))

if __name__ == '__main__':
    interact_main_menu()

'''
Character Sets:
The code defines three character sets:
alpha: Contains lowercase letters from “a” to “z”.
num: Contains digits from “0” to “9”.
special: Contains special characters like “!@#$%&*^|()_+”.
get_available_chars Function:
This function takes two boolean parameters: include_digits and include_special.
It constructs a string called available_chars by combining the alpha set with additional characters based on the input flags.
If include_digits is True, it appends the num set to available_chars.
If include_special is True, it appends the special set to available_chars.
The function returns the combined set of characters.
generate_password Function:
This function generates a random password based on the specified parameters.
It takes the following parameters:
length: Desired password length (default is 16 characters).
mixed_case: Whether to include mixed-case letters (default is False).
include_digits: Whether to include digits (default is False).
include_special: Whether to include special characters (default is False).
It initializes an empty list called password.
It gets the available characters using the get_available_chars function.
For each position in the password (controlled by the range(length) loop):
A random character is chosen from the available_chars.
If mixed_case is True and the character is an alphabet letter, there’s a 50% chance it will be converted to uppercase.
The chosen character is appended to the password list.
Finally, the function joins the characters in the password list to form the final password and returns it.
User Interaction Functions:
interact_main_menu:
This function displays a menu with two options:
Generate a password.
Exit the program.
It repeatedly prompts the user for their choice until they choose to exit.
interact_password_type:
This function prompts the user for password parameters:
Length, whether to use uppercase letters, digits, and special characters.
It then generates and prints a password based on the user’s input.
Main Execution:
The code checks if it’s being run as the main program (i.e., not imported as a module).
If so, it calls interact_main_menu() to start the password generator.
Feel free to try running this code! You can customize the password length and character types according to your preferences. 
'''
