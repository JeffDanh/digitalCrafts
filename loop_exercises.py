# 1 1 to 10
for n in range(1, 11):
    print(n, end=" ")
print()

# 2. n to m
print()
x = int(input("Pick a starting number: "))
y = int(input("Pick an ending number: ")) 
for n in range(x, y + 1):
    print(n, end=" ")
print()

# 3. Odd numbers
print()
for n in range(1, 11):
    if n % 2 != 0:
        print(n, end=" ")
print()

# 4. Print a Square
print()
for n in range(5):
    print("*" * 5)
    
# 5. Print A Square II
print()
s = int(input("Choose the size of the square: "))
for n in range(s):
    print("*" * s)

# 6. Print a Box
print()
height = int(input("Enter height: "))
width = int(input("Enter width: "))
for i in range(height):
    for j in range(width):
        print("*" if i in [0, height-1] or j in [0, width-1] else " ", end="")
    print()

# 7. Print A Triangle
print()
count = 1
while count <= 8:
    print("*" * count)
    count += 2

# 8. Print A Triangle II
print()
h = int(input("Enter triangle height: "))
count = 1
while count <= h:
    print("*" * count)
    count += 1

# 9. Multiplication Table
print()
for n in range(1, 11):
    for l in range(1, 11):
        print(str(n) + " X " + str(l) + " = " + str(n*l))

