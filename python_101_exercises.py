# Exercise 1
print()
name = input('What is your name?')
print('Hello, ' + name)

# Exercise 2
print()
name1 = input('What is your name, again?')
print('HELLO, ' + name1.upper() + '. YOUR NAME HAS ' + str(len(name1)) + ' LETTERS IN IT!')

# Exercise 3
print()
print('Fill in the following blanks: ')
print('____(name)____\'s favorite fruit is ____(fruit)____.')
name = input('What is the name?')
fruit = input('What is the fruit?')
print(name + '\'s favorite fruit is ' + fruit + '.' )

# Exercise 4
print()
day = int(input('Pick a day (0-6): '))
if day == 0:
    print('Sunday')
elif day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thurday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')

# Exercise 5
print()
day = int(input('Pick a day (0-6): '))
if day == 0:
    print('Sleep in')
elif day == 1:
    print('Go to work')
elif day == 2:
    print('Go to work')
elif day == 3:
    print('Go to work')
elif day == 4:
    print('Go to work')
elif day == 5:
    print('Go to work')
elif day == 6:
    print('Sleep in')

# Exercise 6
print()
temp_celsius = int(input('Pick a temperature in C: '))
temp_fahrenheit = temp_celsius * 1.8 + 32
print('That is ' + str(temp_fahrenheit) + ' F.')

# Exercise 7
print()
bill = int(input('What is the total bill amount?'))
service = input('Rate service (good, fair, or bad):')
if service == "good":
    tip = bill * .20
    print('Tip amount: $' + "{:.2f}".format(tip))
elif service == "fair":
    tip = bill * .15
    print('Tip amount: $' + "{:.2f}".format(tip))
elif service == "bad":
    tip = bill * .10
    print('Tip amount: $' + "{:.2f}".format(tip))
total = bill + tip
print('Total amount: $' + "{:.2f}".format(total))

# Exercise 8
print()
bill = int(input('What is the total bill amount?'))
service = input('Rate service (good, fair, or bad):')
split = int(input('Split how many ways?'))
if service == "good":
    tip = bill * .20
    print('Tip amount: $' + "{:.2f}".format(tip))
elif service == "fair":
    tip = bill * .15
    print('Tip amount: $' + "{:.2f}".format(tip))
elif service == "bad":
    tip = bill * .10
    print('Tip amount: $' + "{:.2f}".format(tip))

total = bill + tip
print('Total amount: $' + "{:.2f}".format(total))
cost_per_person = total / split
print('Amount per person: $' + "{:.2f}".format(cost_per_person))






