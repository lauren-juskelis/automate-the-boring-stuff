print('What is your name?')
myName = input()
password = '12345'

if myName == 'Lauren':
    print('What is your password?')
    myPassword = input()
    if myPassword == password:
        print('Entry granted.')
elif myName == 'Jacob':
    print('You are logged in as Lauren. Log in as a different user to access a different account.')
elif myName == 'Mark':
    print('You are logged in as Lauren. Log in as a different user to access a different account.')
else:
    print('Access not granted.')

