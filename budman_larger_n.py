def createList():
    nums = []
    stop = False
   
    while (stop != 'yes'):
        num = int(input('Enter a number for the list: '))
        nums.append(num)
        stop = input('Do you want to stop (yes to stop, enter to continue)? ')
    return nums
def calculate(numList,numCompare):
    greater = []
    for i in range(len(numList)):
        if(numCompare < numList[i]):
            greater.append(numList[i])
    return greater
def askAndReturn():
    n = int(input('Enter the number you would like to compare with: '))
    print(f'The numbers greater than {n} are {calculate(createList(),n)}.')


askAndReturn()
