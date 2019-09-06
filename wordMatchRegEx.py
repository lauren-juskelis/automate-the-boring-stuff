import re, pyperclip

regEx = re.compile(r'''(
(alice | bob | carol) # name
(\s)# space
(eats | pets | throws) # verb
(\s)# space
(apples | cats | baseballs) # noun
(\.) #period
)''', re.VERBOSE | re.IGNORECASE)

text = pyperclip.paste()

print([i[0] for i in regEx.findall(text)])

