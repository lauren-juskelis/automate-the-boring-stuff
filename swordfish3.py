print('What is your name?')
name = input()

while name != 'Joe':
    print('Invalid entry. What is your name?')
    name = input()

print('What is your password?')
password = input()

while password != 'swordfish':
    print('Invalid entry. What is your password?')
    password = input()
    
print('Access granted.')
