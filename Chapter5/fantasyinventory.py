# Fantasy Game Inventory
# Given a player's inventory stored in a dictionary, print the inventory out with item totals and total-total

stuff = {'rope':1, 'torch': 6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        item_total += v
        print(str(v) + " " + k)
    print("Total number of items: " + str(item_total))

displayInventory(stuff)