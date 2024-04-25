r = float(input('Enter the length of the row, in feet: '))
e = float(input('Enter the amount of space, in feet, used by an end-post assembly: '))
s = float(input('Enter the distance, in feet, between each vine: '))

v = (r-(2*e))/s

vines = int(v)

print(f'You have enough space for {vines} vines.')
