days = int(input('Enter the number of days: '))
print(' ---------------------')
print('|   Days   |  Salary  |')
print(' ---------------------')
salary = 1
total = 0
for i in range (1, days+1):
    print(f'|{i:^10}|{salary:^10}|')
    total+=salary
    salary*=2
print(' ---------------------')
dollars = total/100

print(f'After {days} days, the person has made {dollars:.2f} dollars.')
