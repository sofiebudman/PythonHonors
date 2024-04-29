CALORIES_FROM_FAT = 9
CALORIES_FROM_CARBS = 4



def calcCal(type, amount):
    if(type == 'fat'):
        return CALORIES_FROM_FAT * amount
    elif(type == 'carb'):
        return CALORIES_FROM_CARBS*amount
def askAndPrint():
    fatGrams = float(input('Enter how many grams of fat you consumed today: '))
    carbGrams = float(input('Enter how many grabs of carbs you consumed today: '))
    print(f'Your total calories from fat is {calcCal("fat",fatGrams):.2f}.')
    print(f'Your total calories from carbohydrates is {calcCal("carb",carbGrams):.2f}.')

askAndPrint()