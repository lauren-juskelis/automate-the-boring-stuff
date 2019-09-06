# This is a guess the number game. 

import random
number = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

# Give the user three guesses.

for guesses in range(1,4):
    print('Take a guess.')
    guess = int(input())
    if guess < number:
        print('Your guess is too low.')
    elif guess > number:
        print('Your guess is too high.')
    else:
        break

if guess == number:
    print('Good job! You guessed my number in ' + str(guesses) + ' guesses!')
else:
    print('The number I was thinking of was ' + str(number) + '.')
