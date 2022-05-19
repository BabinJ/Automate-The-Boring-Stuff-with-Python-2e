while True:
    age = input('Enter your age: ')
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    password = input('Select a new password (numbers and letters only). ')
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')