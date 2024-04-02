mass = float(input('Please enter the mass of the object: '))

weight = mass*9.8

if(weight>500):
    print(f'An object with a weight of {weight:.2f} and a mass of {mass:.2f} is too heavy.')
elif(weight < 100):
    print(f'An object with a weight of {weight:.2f} and a mass of {mass:.2f} is too light.')
else:
    print(f'The object has a weight of {weight:.2f} and a mass of {mass:.2f}.')
