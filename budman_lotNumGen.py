import random

def generatelotteryNums():
    lotteryNums = []
    for i in range (7):
        lotteryNums.append(random.randint(0,9))
    return lotteryNums

def printLotteryNum(number):   
    for i in range(len(number)):
        print(number[i], end = '')

printLotteryNum(generatelotteryNums())