lst = [-101, 10, -71, 8, 80, -100, 45, 3, 9, 12, 56, 32]

low = None
for element in lst:
    if (low == None or element < low) and element % 2 == 0:
        low = element

print(low)

