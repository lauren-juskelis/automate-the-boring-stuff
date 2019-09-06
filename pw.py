#! python3
#pw.py - An insecure password locker program.

PASSWORDS = {'Umoja': 'Blueskies3!sufjan890!',
             'Inspira': 'bPc-Gk7-ZrN-Zfb',
             'Cigna': 'Blueskies3'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account + '.')
