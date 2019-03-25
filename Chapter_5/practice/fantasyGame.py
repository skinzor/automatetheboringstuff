# Practice: Fantasy Game Inventory

stuff = {}

def displayInventory(inventory):
    item_total = 0
    print(' ')
    print("Inventory:")
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


# Ask 5 items and the amount of each item.
while len(stuff) != 5:
    print('What is the item name?')
    item = input()

    print('How many of them do you have?')
    amount = int(input())
    stuff.setdefault(item, amount)
    # print(stuff)

displayInventory(stuff)




inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addedItems):
    # your code goes here
    totalLoot = len(dragonLoot)
    for i in range (0, totalLoot):
        print(i)
        if dragonLoot[i] in inv:
            inv[dragonLoot[i]] = inv[dragonLoot[i]] + 1
        else:
            inv.setdefault(dragonLoot[i], 1)
    return inv
    
    


inv = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inv)
