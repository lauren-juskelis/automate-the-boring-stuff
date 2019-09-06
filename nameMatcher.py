import pyperclip, re

regEx = re.compile(r'''(
([A-Z][a-z]*)   # first name
(\s)        # space
([A-Z][a-z]*)   # second name
)''', re.VERBOSE)

text = pyperclip.paste()

toPrint = [i[0] for i in regEx.findall(text)]

print(toPrint)
