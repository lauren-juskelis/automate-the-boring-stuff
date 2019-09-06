import pyperclip
import re

text = pyperclip.paste()

regexPhone = re.compile(r'\(\d\d\d\)\s\d\d\d-\d\d\d\d')
regexEmail = re.compile(r'\S{1,}@\w{1,}\.\w\w\w')

phones = regexPhone.findall(text)
emails = regexEmail.findall(text)

if phones == []: print('No phone numbers found.')
if emails == []: print('No emails found.')

PAE = phones + emails

pyperclip.copy(str(PAE))
