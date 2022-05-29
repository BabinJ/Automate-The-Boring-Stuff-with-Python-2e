# Regex Version of the strip() method

# regexStrip.py - With no arguments, strips whitespace from beginning and end # of string. With argument, removes argument characters from the string.

import re

# Define function to strip or sub from string
def regstrip(text, sub=''):

    # Define regexes
    stripRegex = re.compile(r'^\s*(.*)\s*$')
    subRegex = re.compile(r'[.*(%s).*]'%sub)
    
    if sub == '':
        reducedText = stripRegex.search(text)
        print(reducedText[0])
    else: 
        reducedText = subRegex.sub('',text)
        print(reducedText)

userString = input('Enter text to strip/sub from: ')
replacement = input('If a specific text to be removed, enter it here: ')
if replacement != '' :
    regstrip(userString, replacement)
else: 
    regstrip(userString)