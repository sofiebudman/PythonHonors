startingWeight = float(input('Enter your starting weight: '))
print(' --------------------------------------')
print('|   Months Passed   |   Weight (lbs)   |')
print(' --------------------------------------')
for i in range (1,7):
    newWeight = startingWeight - (i*4)
    print(f'|{i:^19}|{newWeight:>18.2f}|')
print(' --------------------------------------')
