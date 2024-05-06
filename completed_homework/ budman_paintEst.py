
FEET_PER_GALLON = 112
LABOR_HOURS = 8
LABOR_CHARGE = 35

def calc(feet,pricePerGallon):
    numGallons = feet/FEET_PER_GALLON
    numHours = (feet/FEET_PER_GALLON)*LABOR_HOURS
    costPaint = numGallons*pricePerGallon
    laborCharge = LABOR_CHARGE *numHours
    total = costPaint+laborCharge
    return[numGallons,numHours,costPaint,laborCharge,total]

def show():
    feet = int(input('Enter the number of square feet of the wall space to be painted: '))
    pricePerGallon = float(input('Enter the price per gallon of paint: '))
    result = calc(feet,pricePerGallon)
    print(f'The paint job will {result[0]:.2f} gallons of paint.')
    print(f'The paint job will need {result[1]:.2f} hours of labor.')
    print(f'The paint will cost ${result[2]:.2f}.')
    print(f'The labor will cost {result[3]:.2f}.')
    print(f'The total cost of this paint job will be ${result[4]:.2f}.')

show()