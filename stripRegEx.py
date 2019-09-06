import re

def reverse_slicing(string):
    return string[::-1]

def myStrip(string, param = ' '):
    regEx1 = re.compile(r'^' + re.escape(param))
    first = regEx1.sub('', string)
    regEx2 = re.compile(re.escape(reverse_slicing(param)) + r'$')
    found = regEx2.sub('', first)
    return found

string = ' the cat and the hat '

print(myStrip(string, ' t'))
