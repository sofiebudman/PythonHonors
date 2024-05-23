date = input('Enter a date in the form of mm/dd/yyyy: ')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December']
monthSlice = slice(2)
month = date[monthSlice]
daySlice = slice(3,5)
yearSlice = slice(6,10)
print(f'{months[int(month)-1]} {date[daySlice]}, {date[yearSlice]}')


