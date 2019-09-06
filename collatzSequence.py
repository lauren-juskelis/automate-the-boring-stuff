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
enteredNumber = int(input())

# Perform Collatz sequence on user's number:
while enteredNumber != 1:
    enteredNumber = int(collatz(enteredNumber))
    
