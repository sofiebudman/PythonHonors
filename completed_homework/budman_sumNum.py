num = int(input('Enter a positive number (negative to quit): '))
sum = 0
while (num >=0):
    sum +=num
    num = int(input('Enter a positive number (negative to quit): '))
print(f'The sum of all the number entered is {sum}')
