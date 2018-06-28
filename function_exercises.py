# 1. Hello
def hello(name):
    return "Hello, " + name
print(hello('Jeff'))

# 2. y = x+ 1
print()
import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

# 3. Square of x
import matplotlib.pyplot as plot

def f(x):
    return x * x

xs = list(range(-100, 101))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

# 4. Odd or Even
import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xs = list(range(-5, 6))
ys = []

for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()

# 5. Sine
import math
import matplotlib.pyplot as plot

def f(x):
    return math.sin(x)

xs = list(range(-5, 6))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

# 6. Sine 2
from numpy import arange
import math
import matplotlib.pyplot as plot

def f(x):
    return math.sin(x)

xs = list(arange(-5, 6, 0.1))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

# 7. Degree Conversion
def temp(temp_c):
    temp_f = temp_c * 1.8 + 32
    return temp_f

celcius = 23
fahrenheit = temp(celcius)

xs = list(range(celcius, int(fahrenheit)))
ys = []

for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

# 8. Play again?
def ask():
    ans = input("Do you want to play again (y or n)? ")
    if ans == "y" or "Y":
        return True
    else:
        return False

print(ask())

# 9. Play again? Again.
def ask_again():
    unanswered = True
    while unanswered == True:
        ans_again = input("Do you want to play again (Y or N)?")
        if ans_again == "Y":
            return True
            unanswered = False
        elif ans_again == "N":
            return False
            unanswered = False
        else:
            print("Invalid input.")

print(ask_again())


