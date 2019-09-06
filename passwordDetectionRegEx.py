import re, pyperclip

def length(password):
    if len(password) >= 8:
        return True
    else:
        return False

def upper(password):
    regEx = re.compile(r'[A-Z]')
    result = regEx.search(password)
    if result != None:
        return True
    else:
        return False

def lower(password):
    regEx = re.compile(r'[a-z]')
    result = regEx.search(password)
    if result != None:
        return True
    else:
        return False 

def digit(password):
    regEx = re.compile(r'[0-9]')
    result = regEx.search(password)
    if result != None:
        return True
    else:
        return False

def spaces(password):
    regEx = re.compile(r'\s')
    result = regEx.search(password)
    if result != None:
        return False
    else:
        return True

def test(password):
    if length(password) == True and upper(password) == True and lower(password) == True and digit(password) == True and spaces(password) == True:
        return True
    else:
        return False

pw = pyperclip.paste()

if test(pw) == True:
    print("'" + str(pw) + "' is a valid password.")
else:
    print("'" + str(pw) + "' is not a valid password.")
