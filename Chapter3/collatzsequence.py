# Build a program to run the Collatz sequence on a user-input value

import sys

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    return result

try:
    while True:
        inputValue = input("Enter a number (or q to quit): \n")
        if inputValue == 'q':
            sys.exit()
        elif int(inputValue) != 0:
            inputValue = int(inputValue)
            break
        else:
            print('The Collatz sequence does not work with 0. Please choose a positive integer.')
        
    result = collatz(inputValue) # Run initial collatz function to determine if result is already 1
    print(result) # Print output of initial collatz function run

    if result != 1: #
        while result != 1:
            result = collatz(result)
            print(result)
    else:
        print(result)

except (TypeError, ValueError):
    print("Only a number (or q to quit) may be entered. ")
    sys.exit()