#! python3

birthdays = {'Lauren': '09/25/1992', 'Izebel': '08/06/1985', 'Matthew': '04/21/1994'}

while True:
    print('Enter a name (or blank to quit).')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is ' + name + 's birthday.')
    else:
        print('I do not have birthday information for ' + name + '. What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
