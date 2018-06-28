# 1 Sum the Numbers
a1 = [1, 2, 3, 4, 5]
print(sum(a1))

# 2 Largest Number
print()
a2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max(a2))

# 3 Smallest Number
print()
a3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(a3))

# 4 Even Numbers
print()
a4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in a4:
    if n % 2 == 0:
        print(n)

# 5 Positive Numbers
print()
a5 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for n in a5:
    if n > 0:
        print(n)

# 6 Positive Numbers II
print()
a6 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
new_a6 = []
for n in a6:
    if n > 0:
        new_a6.append(n)
print(new_a6)

# 7 Multiply a list
print()
a7 = [1, 2, 3, 4, 5]
factor = 2
new_a7 = []
for n in a7:
    new_a7.append(n * factor)
print(new_a7)

# 8 Multiply Vectors
print()
a8 = [1, 2, 3]
b8 = [4, 5, 6]
new_a8 = [a*b for a,b in zip(a8, b8)]
print(new_a8)

# 9 Matrix Addition
print()
a9 = [[1, 2], [3, 4]]
b9 = [[5, 6], [7, 8]]
result = [[0, 0], [0, 0]]
for i in range(len(a9)):
    for j in range(len(a9[0])):
        result[i][j] = a9[i][j] + b9[i][j]
for r in result:
    print(r)

# 10 Matrix addition II
print()
a10 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b10 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(a10)):
    for j in range(len(a10[0])):
        result[i][j] = a10[i][j] + b10[i][j]
for r in result:
    print(r)

# 11. De-dup
print()
a11 = [1, 1, 2, 2, 3, 3, "Jeff", "Jeff"]
new_a11 = []
for n in a11:
    if n not in new_a11:
        new_a11.append(n)
print(new_a11)









