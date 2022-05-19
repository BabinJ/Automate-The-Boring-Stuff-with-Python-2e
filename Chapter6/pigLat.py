# English to Pig Latin
# pigLat.py  - Takes a phrase and converts it to pig latin

print('Enter the English message to be translated into Pig Latin: ')
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] # A list of the words in Pig Latin

for word in message.split(): # Loop through the words in the message
    # Separate the non-letters at the start of the word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue

    # Separate the non-letters at the end of the word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    
    # Remember if the word was in uppercase or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    # Make the word lowercase for translation
    word = word.lower()

    # Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'


    # Set the hword back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    # Add the non-letters back to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    
# Join all the words back together into a single string:
print(' '.join(pigLatin))