#! python
# bulletPointAdder.py - Adds Wikipedia bullets to the start of each line of text in the clipboard and outputs into clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Import text and add stars
lines = text.split(sep='\n')
for i in range(len(lines)):  #loop through all list items (lines) in text
    lines[i] = '* ' + lines[i]  #add a star to each item by index
text = '\n'.join(lines)

pyperclip.copy(text)