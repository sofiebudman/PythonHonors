import math
budget = float(input('Enter amount budgeted for the month: '))
amount = float(input('Enter an amount spent(0 to quit): '))
spent = 0
while(amount!=0):
    spent +=amount
    amount = float(input('Enter an amount spent(0 to quit): '))
print(f'Budgeted: $ {budget:.2f}')
print(f'Spent : $ {spent:.2f}')

difference = math.fabs(budget-spent)
if(budget > spent):
    print(f'You are $ {difference:.2f} under budget. GOOD JOB!')
elif(budget == spent):
    print('You spent your exact budget. Try to be under next time!')
else:
    print(f'You are ${difference:.2f} over budget. PLAN BETTER NEXT TIME!')
