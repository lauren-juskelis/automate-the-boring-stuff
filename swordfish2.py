while True:
    print('What is your name?')
    name = input()
    if name != 'Joe':
        continue
    if name == 'Joe':
        break

while True:
    print('What is your password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
    
print('Access granted.')
