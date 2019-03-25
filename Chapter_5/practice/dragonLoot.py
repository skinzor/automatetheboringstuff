inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(i, a):
    totalItems = 0
    print('')
    print('Inventory:')
    
    for i, a in inv.items():
        print(str(a) + ' ' + i)
        totalItems = totalItems + a
    print('Total number of items: ' + str(totalItems))


def addToInventory(inventory, addedItems):
    # your code goes here
    totalLoot = len(dragonLoot)
    for i in range (0, totalLoot):
        if dragonLoot[i] in inv:
            inv[dragonLoot[i]] = inv[dragonLoot[i]] + 1
        else:
            inv.setdefault(dragonLoot[i], 1)
    return inv
    
    


inv = addToInventory(inv,dragonLoot)
print(inv)
displayInventory(inv, dragonLoot)

# print(addToInventory(inv, dragonLoot))
# displayInventory(inv)
