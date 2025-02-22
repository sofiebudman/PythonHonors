def calc(rainData):
    months = ['January','February', 'March','April','May','June','July','August','September','October','November','December']
    maxRain = max(rainData)
    maxIndex = [i for i, val in enumerate(rainData) if val == maxRain]
    maxMonths = [months[i] for i in maxIndex]

    minRain = min(rainData)
    minIndex = [j for j, val in enumerate(rainData) if val == minRain]
    minMonths = [months[j] for j in minIndex]

    return [maxMonths,minMonths]
      
def askAndReturn():
    rain = [float(input('Enter the amount of rainfall in January: ')),float(input('Enter the amount of rainfall in February: ')),float(input('Enter the amount of rainfall in March: ')),float(input('Enter the amount of rainfall in April: ')),float(input('Enter the amount of rainfall in May: ')),float(input('Enter the amount of rainfall in June: ')),float(input('Enter the amount of rainfall in July: ')),float(input('Enter the amount of rainfall in August: ')),float(input('Enter the amount of rainfall in September: ')),float(input('Enter the amount of rainfall in October: ')),float(input('Enter the amount of rainfall in November: ')),float(input('Enter the amount of rainfall in December: '))]
    print(f'The total rainfall for the year is: {sum(rain):.2f} inches.')
    print(f'The average rainfall for the year is: {sum(rain)/len(rain):.2f} inches.')
    print(f'The month(s) with the highest rain is/are {", ".join(calc(rain)[0])} with {max(rain):.2f} inches.')
    print(f'The month(s) with the least rain is/are {", ".join(calc(rain)[1])} with {min(rain):.2f} inches.')


askAndReturn()