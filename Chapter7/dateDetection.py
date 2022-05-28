# Date Detection
# dateDetection.py - Extracts dates from the clipboard, and pastes those values back into the clipboard

import pyperclip, re

# Regex for grabbing date values
dateRegex = re.compile(r'''(
    (0[1-9]|1[0-9]|2[0-9]|3[0-1])+        # Day
    /               # Slash
    (0[1-9]|1[0-2])+        # Month
    /               # Slash
    (1[0-9][0-9][0-9]|2[0-9][0-9][0-9])+    # Year
)''', re.VERBOSE)

# Bring in the clipboard text
text = str(pyperclip.paste())

# Combine date fields as DD/MM/YYYY and append, validating first. Define 30- and 31-day months
matches=[]
shorts = [4,6,9,11]
longs = [1,3,5,7,8,10,12]

# Run regex on the text, and pull out dates
for group in dateRegex.findall(text):
    day = int(group[1])
    month = int(group[2])
    year = int(group[3])
    dayMonth = str(day) + "/" + str(month)
    date = '/'.join([group[2],group[1],group[3]])

    # Define a leap-year check for use with February 29th dates
    leapYearCheck = (((year % 4 == 0) and (year % 100 != 0)) or ((year % 4 ==0) and (year % 100 == 0) and (year % 400 ==0)))

    # Check dates for errors (30-day months with a 31st, or non-leap-year February 29th), and load dates (plus applicable invalid date messages) to matches list
    if ((month in shorts) and (day>30)):
        message = 'Month/day combination %s not valid for' % (dayMonth)
        matches.append(message)
    elif ((month == 2) and (day > 28) and not leapYearCheck):
        message = '%s is not a valid leap year date.' % (date)
        matches.append(message)
    else:
        matches.append(date)

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No valid/properly formatted dates found.')