# Strong Password Detection
# passwordStrength.py - Checks password to ensure it meets certain criteria:
# -At least 8 characters long, 1 uppercase, 1 lowercase, 1 digit

#Import modules
import re

# Create regexes
lowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
digitRegex = re.compile(r'[0-9]')
lengthRegex = re.compile(r'^[a-zA-Z0-9]{8,}$')

# Function to check entered password against regexes
def pwcheck():
    while True:
        password = input('Please enter a new password: ')
        lowerMO = lowerRegex.search(password)
        upperMO = upperRegex.search(password)
        digitMO = digitRegex.search(password)
        lengthMO = lengthRegex.search(password)
        if lowerMO and upperMO and digitMO and lengthMO:
            print('Password saved!')
            break
        else: 
            print('Password does not match minimum specs. Please try again.')
            continue

# Get user input and pass to pwcheck function
pwcheck()