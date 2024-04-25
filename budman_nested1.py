
for rows in range(8):
    for columns in range(rows+1):
        print('*', end = '')
    print()

print()
for rows in range(8):
    for columns in range(8-rows, 0, -1):
        print('*', end = '')

    print()
