# Sandwich Maker
# sandwichMaker.py - use inputMenu() multiple times to build a sanchwich

import pyinputplus as pyip

def sandwichGen():

    #Get desired ingredients from user
    ingredients = []
    bread = pyip.inputMenu(['Wheat','White','Sourdough'])
    ingredients.append(bread)

    protein = pyip.inputMenu(['Chicken','Turkey','Ham','Tofu'])
    ingredients.append(protein)

    cheeseYN = pyip.inputYesNo('Would you like cheese? ')
    if cheeseYN == 'yes':
        cheese = pyip.inputMenu(['Cheddar','Swiss','Mozzarella'])
        ingredients.append(cheese)

    for i in ['Mayo','Mustard','Lettuce','Tomato']:
        response = pyip.inputYesNo('Would you like %s? ' % i)
        if response == 'yes':
            ingredients.append(i)

    #Calculate price using pricelist and selections
    priceList = {
        'Wheat':1.25, 'White':1, 'Sourdough':1.50,
        'Chicken': 2, 'Turkey': 2.15, 'Ham': 1.75, 'Tofu': 2.50,
        'Cheddar': 1, 'Swiss': 1.25, 'Mozarella': 1.20,
        'Mayo': 0.5, 'Mustard': 0.25, 'Lettuce': 0.15,'Tomato': 0.25
    }
    
    price = 0
    for item in ingredients:
        price += priceList[item]

    print('Thank you. That will be $%.2f.' % price)

sandwichGen()