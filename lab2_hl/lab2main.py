"""
Author: Haoyun Luo & Monobina Saha
CIS 22C Lab 2
"""

from Dollar import Dollar
from Pound import Pound
from Currency import Currency

def main():
    currency_arr = [Currency, Currency]
    currency_arr[0] = Pound()
    currency_arr[1] = Dollar()
    
    currency_arr[0].print()
    currency_arr[1].print()
    # new line
    print()
    
    print_balance = True
    
    while True:
        try:
            user_input = input()
            
            if user_input[0] == "q":
                print_balance = False
                break
            
            # split the string along the spaces to get a list of commands
            # manual implementation of str.split() in case it is not allowed
            input_commands = []
            current_word = ""
            for char in user_input:
                if char.isspace() and current_word != "":
                    input_commands.append(current_word)
                    current_word = ""
                else:
                    current_word += char
            if current_word != "":
                input_commands.append(current_word)
                    
            # assume that the user input is always in the correct format
            operation = input_commands[0]
            operand = input_commands[1]
            amount = float(input_commands[2])
            amount_currency = input_commands[3]
            
            # second object to add or subtract from the first one
            modification_object = Pound(amount) if amount_currency == "pound" else Dollar(amount)
            
            
            if operation == "a":
                if operand == "p":
                    currency_arr[0].add(modification_object)
                elif operand == "d":
                    currency_arr[1].add(modification_object)
                
            elif operation == "s":
                if operand == "p":
                    currency_arr[0].subtract(modification_object)
                elif operand == "d":
                    currency_arr[1].subtract(modification_object)
                    
        except ValueError as value_error_message:
            print(value_error_message)
        except TypeError as type_error_message:
            print(type_error_message)
        finally:
            if print_balance:
                currency_arr[0].print()
                currency_arr[1].print()
                # new line
                print()
            
        
if __name__ == "__main__":
    main()