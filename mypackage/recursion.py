
def sum_array(array):
    value = 0
    for i in array:
        value += i
    return value
    '''Return sum of all items in array'''


def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


def factorial(n):
    '''Return n!'''
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    return word[::-1]
