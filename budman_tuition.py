tuition = 8000
print('Year      Projected Tuition (perSemester)')
print('-----------------------------------------')
for i in range(1,6):
    tuition *= 1.03
    print(f'{i:<10}${tuition:<.2f}')
    
