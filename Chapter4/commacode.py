spam = ['apples','bananas','tofu','cats']


def commasep(listIn):
    for i in range(len(listIn)):
        if i == 0:
            printstring = str(listIn[i]) + ', '
        elif (i > 0 and i < (len(listIn) -1)):
            printstring = printstring + str(listIn[i]) + ', '
        else:
            printstring = printstring + 'and ' + str(listIn[i])
    return printstring

spamOut = commasep(spam)
print(spamOut)