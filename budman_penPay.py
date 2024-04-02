days = int(input('Enter the number of days: '))
print(' ---------------------')
print('|   Days   |Salary($)|')
print(' ---------------------')
salary = 0.01
total = 0
for i in range (1, days+1):
    print(f'|{i:^10}|{salary:^9.2f}|')
    total+=salary
    salary*=2
print(' ---------------------')


print(f'After {days} days, the person has made {total:.2f} dollars.')
