def listToString(usersList):
    returnedString = ''
    for i in range(0,len(usersList)):
        if i < (len(usersList) - 1):
            returnedString += str(usersList[i]) + ', '
        else:
            returnedString += 'and ' + str(usersList[i])
    return returnedString

spam = [1,3,4,5,6]
toPrint = listToString(spam)
print(toPrint)
