import pyperclip
import re

text = pyperclip.paste()

regexPhone = re.compile(r'''(
    (\(\d{3}\)\s|\d{3}(\s|\.|\-))?  # area code
    (\d{3})                         # first three digits
    (\s|\.|\-)                      # separator
    (\d{4})                         # last four digits
    (\s(EXT.|ext.|x)\s*(\d{1,5}))?  # extension 
)''', re.VERBOSE)

regexEmail = re.compile(r'''(
    (\S{1,})        # part before @
    (@)             # the @
    (\w{1,})        # email server
    (\.\w{3})       # .com, .org, etc.
)''', re.VERBOSE)

phones = [i[0] for i in regexPhone.findall(text)]
emails = [i[0] for i in regexEmail.findall(text)]

if phones == []: print('No phone numbers found.')
if emails == []: print('No emails found.')

PAE = phones + emails

pyperclip.copy(str(PAE))

print('Copied to clipboard: ')
print(PAE)
