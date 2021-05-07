

# task1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error.

list1 = [123, 124, 124]


def oops1():
    return (list1[4])


def exception1():
    try:
        print(oops1())
    except IndexError:
        return 'Oooops'


print(exception1())

# What happens if you change oops to raise KeyError instead of IndexError?

dict1 = {'key': 1}


def oops2():
    return (dict1['kkeyy'])


def exception2():
    try:
        print(oops2())
    except IndexError:
        return 'Oooops'


print(exception2())

# task2
# Write a function that takes in two numbers from the user via input(),
# call the numbers a and b, and then returns the value of squared a divided by b,
# construct a try-except block which raises an exception if the two values given by the input function were not numbers,
# and if value b was zero (cannot divide by zero).

while ValueError:
    try:
        a = int(input('Type the first number'))
        break
    except ValueError:
        print('Numbers only')
while ValueError:
    try:
        b = int(input('Type the second number'))
        break
    except ValueError:
        print('Numbers only bruh')


def math(x, y):
    try:
        return x ** 2 / y
    except ZeroDivisionError:
        print('FATAL ERROR : Cannot divide by zero')


print(math(a, b))
