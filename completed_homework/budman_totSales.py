
def calculate(sales):
    total= 0
    for i in range (len(sales)):
        total += sales[i]
    return total

def askAndReturn():
    sales = [float(input('Enter the sales for Monday: ')),float(input('Enter the sales for Tuesday: ')),float(input('Enter the sales for Wednesday: ')),float(input('Enter the sales for Thursday: ')),float(input('Enter the sales for Friday: ')),float(input('Enter the sales for Saturday: ')),float(input('Enter the sales for Sunday: '))]
    print(f'The total sales for that week is ${calculate(sales):.2f}.')
askAndReturn()
