print('What is your name?')
name = input()

while name != 'Joe':
    print('Invalid entry. What is your name?')
    name = input()

print('What is your password?')
password = input()

if password == 'swordfish':
    print('Access granted.')
else:
    print('Access denied.')
