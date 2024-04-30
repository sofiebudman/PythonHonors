import random

def askAndReturn():
    num1 = random.randint(0,999)
    num2 = random.randint(0,999)
    print(f'{num1} + {num2}')
    ans = int(input('Enter the answer to the addition: '))
    check(num1,num2,ans)


def check(num1,num2, ans):
    if(num1+num2 == ans):
        print('Congrulations! That was correct.')
    else:
        print(f'That was incorrect, the correct answer is {num1+num2}.')
 
askAndReturn()
