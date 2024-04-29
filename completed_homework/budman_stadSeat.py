def calculate(a,b,c):
    return a*20 + b*15 + c*10

def userInput():
    numSeatsA = int(input('Enter how many Class A seats were sold: '))
    numSeatsB = int(input('Enter how many Class B seats were sold: '))
    numSeatsC = int(input('Enter how many Class C seats were sold: '))
    total = calculate(numSeatsA, numSeatsB, numSeatsC)
    print(f'The amount of income from these ticke sales is ${total:,.2f}')

                    
userInput()
