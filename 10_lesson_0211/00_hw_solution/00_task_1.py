lst = [4, 10, 4, 8, 0, 4, 0, 3, 9, 12, 56, 0]

middle = sum(lst) / len(lst)

for i in range(len(lst)):
    if lst[i] == 0:
        lst[i] = middle

print(lst)

