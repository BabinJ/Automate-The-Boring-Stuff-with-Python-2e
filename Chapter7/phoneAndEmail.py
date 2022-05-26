# Phone Number and Email Extractor
# phoneAndEmail.py - Extracts phone numbers and emails from the clipboard, and pastes only those values back into the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # Area code
    (\s|-|\.)?                      # Separator
    (\d{3})                         # First three digits
    (\s|-|\.)                       # Separator
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Extension
)''', re.VERBOSE)

# Create Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # Username
    @                               # The @ symbol
    [a-zA-Z0-9.-]+                   # The domain name
    (\.[a-zA-Z]{2,4})               # dot something (e.g. .com, .gov, .net, .ca)
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the cliipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')