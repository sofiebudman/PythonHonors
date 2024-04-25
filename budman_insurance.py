
def calculateInsurance(cost):
    return 0.8*cost

def run():
    replacementCost = float(input('Enter the replacement cost of your building: '))
    insuranceAmount = calculateInsurance(replacementCost)
    print(f'You should buy at least ${insuranceAmount:,.2f} of insurance.')

run()
