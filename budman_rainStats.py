
rain = [float(input('Enter the amount of rainfall in January: ')),float(input('Enter the amount of rainfall in February: ')),float(input('Enter the amount of rainfall in March: ')),float(input('Enter the amount of rainfall in April: ')),float(input('Enter the amount of rainfall in May: ')),float(input('Enter the amount of rainfall in June: ')),float(input('Enter the amount of rainfall in July: ')),float(input('Enter the amount of rainfall in August: ')),float(input('Enter the amount of rainfall in September: ')),float(input('Enter the amount of rainfall in October: ')),float(input('Enter the amount of rainfall in November: ')),float(input('Enter the amount of rainfall in December: ')),]
months = ['January','February', 'March','April','May','June','July','August','September','October','November','December']

print(f'The total rainfall for the year is: {sum(rain):.2f} inches.')
print(f'The average rainfall for the year is: {sum(rain)/len(rain):.2f} inches.')
print(f'The month with the highest rain is {months[rain.index(max(rain))]} inches.')
print(f'The month with the least rain is {months[rain.index(min(rain))]} inches.')

      
