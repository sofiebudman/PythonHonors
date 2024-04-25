subtotal = float(input('Enter the charge for food: '))
tip = subtotal * 0.18
salesTax = subtotal * 0.07
total = subtotal + tip + salesTax
print(f'The total price of ${subtotal:.2f} of food, a ${tip:.2f} tip, and a ${salesTax:.2f} sales tax is ${total:.2f}.')
