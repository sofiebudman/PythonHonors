years = int(input('Enter the number of years: '))
total = 0

for i in range(years):
    for j in range(12):
        inches = float(input('Enter how many inches it rained this month: '))
        total +=inches
months = years*12
average = total / months

print(f'After {months} months, the total rainfall was {total:.2f} inches with an average of {average:.2f} inches per month.')
