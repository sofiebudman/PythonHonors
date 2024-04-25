cost = float(input('Enter the amount of the purchase: '))
stateTax = cost *0.05
countyTax = cost* 0.025
total = cost+stateTax+countyTax
print(f'Purchase Amount: {cost:.2f}')
print(f'-State Tax: {stateTax:.2f}')
print(f'-County Tax: {countyTax:.2f}')
print(f'-Sale Total: {total:.2f}')
