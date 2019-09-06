import pyperclip, re

commaRegex = re.compile(r'''(
(\D(\d{3}|\d{2}|\d)(\s|\,))     # first chunk
((\d{3}|\d{2}|\d)(\s|\,|\.))*   # second chunk
)''', re.VERBOSE)

text = pyperclip.paste()

commas = [i[0] for i in commaRegex.findall(text)]

nc = []

for i in range(len(commas)):
    nc.append(commas[i][1:-1])

print(nc)
