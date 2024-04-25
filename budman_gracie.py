lat = (40.59, 40.52, 40.621, 40.519, 40.56, 41.265, 40.61, 40.806, 41.259, 41.265, 41.264, 41.264, 41.259, 41.262, 41.263)

lon = (69.532, 69.419, 69.354, 69.263, 69.478, 70.805, 69.706, 70.331, 70.815, 70.823, 70.815, 70.81, 70.824, 70.811, 70.811)

n = max(lat)
s = min(lat)
e = min(lon)
w = max(lon)

print('Farthest North = ' + str(n))
print('Farthest West = ' + str(w))
print('Farthest South = ' + str(s))
print('Farthest East = ' + str(e))
