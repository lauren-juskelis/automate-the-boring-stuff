playerOneInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(item):
    return(str(playerOneInventory[item]))

def invTotal():
    totalItems = 0
    for k in playerOneInventory.keys():
        totalItems = totalItems + playerOneInventory[k]
    return(str(totalItems))

print('You have:')
print(' - Arrow: ' + displayInventory('arrow'))
print(' - Gold coin: ' + displayInventory('gold coin'))
print(' - Rope: ' + displayInventory('rope'))
print(' - Torch: ' + displayInventory('torch'))
print(' - Dagger: ' + displayInventory('dagger'))
print('Total number of items: ' + invTotal())


