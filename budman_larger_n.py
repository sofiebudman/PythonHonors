
def calculate(numList,numCompare):
    greater = []
    for i in range(len(numList)):
        if(numCompare < numList[i]):
            greater.append(numList[i])
    return greater
def askAndReturn():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    n = int(input('Enter the number you would like to compare with: '))
    print(f'The numbers greater than {n} are {calculate(nums,n)}.')


askAndReturn()
