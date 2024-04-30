print('|  Time  |  Falling Distance  |')
def falling_distance(time):
    distance = (0.5)*(9.8)*(time**2)
    return distance
for i in range (1,11):
   
    print(f'|{i:^8}|{ falling_distance(i):^20.0f}|')
