# Define the Collatz function:
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    else:
        print(number * 3 + 1)
        return(number * 3 + 1)
        
# Ask the user for a number:
print('Enter a number.')

# Perform Collatz sequence on user's number:
try:
    enteredNumber = int(input())
    while enteredNumber != 1:
        enteredNumber = int(collatz(enteredNumber))
except ValueError:
    print('Please enter a whole integer.')
