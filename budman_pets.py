pet = input('Enter a pet you have(enter rock to quit): ')
num = 1
while(pet != 'rock'):
    print(f'You have a {pet} for a total of {num} pet(s).')
    pet = input('Enter a pet you have(enter rock to quit): ')
    num +=1
    
