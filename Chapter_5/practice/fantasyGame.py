# Practice: Fantasy Game Inventory

stuff = {}

def displayInventory(i, a):
    totalItems = 0
    print('')
    print('Inventory:')
    
    for i, a in stuff.items():
        print(str(a) + ' ' + i)
        totalItems = totalItems + a
    print('Total number of items: ' + str(totalItems))


# Ask 5 items and the amount of each item.
while len(stuff) != 5:
    print('What is the item name?')
    item = input()

    print('How many of them do you have?')
    amount = int(input())
    stuff.setdefault(item, amount)
    # print(stuff)

displayInventory(item, amount)
