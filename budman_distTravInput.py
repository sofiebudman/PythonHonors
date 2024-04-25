speed = int(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))
print('Hour        Distance Traveled')
d = 0
for i in range (1, hours + 1):
    d += speed
    print(f'{i:^5}{d:>16}')
    
