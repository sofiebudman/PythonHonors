def enterCost():
    loan = int(input('Enter the monthly loan amount: '))
    insurance = int(input('Enter the monthy insurance amount: '))
    gas = int(input('Enter the monthly gas amount: '))
    oil = int(input('Enter the monthly oil amount: '))
    tires = int(input('Enter the monthly tires amount: '))
    maintenance = int(input('Enter the monthly maintenance amount: '))
    return loan+insurance+gas+oil+tires+maintenance
    

def displayCost():
    monthlyExpense = enterCost()
    annualExpense = 12*monthlyExpense
    print(f'Total monthly expense: ${monthlyExpense:,.2f}')
    print(f'Total annual expense: ${annualExpense:,.2f}')
    
displayCost()
