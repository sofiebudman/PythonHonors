alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
values = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

string = input('Enter a string: ')

for i in range(len(string)):
    if(string[i].isalpha()):
        values[alphabet.index(string[i].upper())] +=1

print(f'The most frequent character is {alphabet[values.index(max(values))]}.')
