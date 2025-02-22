def askAndPrint():
    nums = []
    for i in range(20):
        num = int(input('Enter a number: '))
        nums.append(num)
    print(f'The lowest number in the list is {calculate(nums)[0]}.')
    print(f'The highest number in the list is {calculate(nums)[1]}.')
    print(f'The total of the numbers in the list is {calculate(nums)[2]}.')
    print(f'The average of the numbers in the list is {calculate(nums)[3]:.2f}.')

def calculate(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return min(nums),max(nums), total,total/len(nums)

askAndPrint()
