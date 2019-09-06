dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
playerInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return(inventory)

def displayInventory(dictionary):
    total = 0
    print('Inventory:')
    for k, v in dictionary.items():
        total = total + v
        print(' - ' + k + ': ' + str(v))
    print('Total items: ' + str(total))

displayInventory(addToInventory(playerInventory, dragonLoot))
        
