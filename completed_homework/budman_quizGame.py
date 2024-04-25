import math
numPennies = int(input('Enter the number of pennies: '))
numNickels = int(input('Enter the number of nickels: '))
numDimes = int(input('Enter the number of dimes: '))
numQuarters = int(input('Enter the number of quarters: '))

total = 0.01*numPennies + 0.05 * numNickels + 0.1*numDimes + 0.25 *numQuarters
difference = math.fabs(1 - total)
if(numPennies <0 or numNickels < 0 or numDimes < 0 or numQuarters < 0):
    print(f'You cannot have a negative number of coins. Restart the program and try again!')
elif(total == 1):
    print(f'Congratulations you won the game!')
elif(total > 1):
    print(f'You did not win. Your total is ${total:.2f} which is over by ${difference:.2f}.')
else:
    print(f'You did not win. Your total is ${total:.2f} which is under by ${difference:.2f}.')
