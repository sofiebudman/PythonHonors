def askAndPrint():
    num = int(input('Enter a postive integer: '))
    while(num<=0):
        num = int(input('Try again, enter a postive integer: '))
    numList= []
    for i in range(1,1+num):
        numList.append(i)
    print(f'The sum of the even numbers between 1 and {num} is {calc(numList)}.')
    

def calc(numList):
    evens = []
    for i in range(len(numList)):
        if(numList[i] %2 == 0):
            evens.append(numList[i])
    sumEven = 0
    for i in range(len(evens)):
        sumEven +=evens[i]
    return sumEven
    
askAndPrint()

        
        
