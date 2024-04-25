import random
num = random.randrange(1,100)
guess = int(input('Guess a number between 1 and 100: '))
while (guess!=num):
    if(guess>num):
        print(f'{guess} is too high.')
        guess = int(input('Guess a number between 1 and 100: '))
    elif(guess<num):
        print(f'{guess} is too low.')
        guess = int(input('Guess a number between 1 and 100: '))

print(f'Congratulations! {guess} was the number.')

    
