#! python
# bulletPointAdder.py - Adds Wikipedia bullets to the start of each line of text in the clipboard and outputs into clipboard

import pyperclip
text = pyperclip.paste()

# TODO: Import text and add stars
text = text.split(sep='/n')
("*/n").join(text)

pyperclip.copy(text)
