sales = [int(input('Enter the sales for Monday: ')),int(input('Enter the sales for Tuesday: ')),int(input('Enter the sales for Wednesday: ')),int(input('Enter the sales for Thursday: ')),int(input('Enter the sales for Friday: ')),int(input('Enter the sales for Saturday: ')),int(input('Enter the sales for Sunday: '))]
total= 0
for i in range (len(sales)):
    total += sales[i]


print(f'The total sales for that week is {total}.')
