#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "Bryan"


def add(x, y):
    """Add two integers. Handles negative values."""
    # your code here
    result = x + y
    return result

def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    # your code here
    result = 0
    count = 0

    apple_x = x
    bear_y = y

    if x < 0:
        apple_x = -apple_x  #turn positive
    elif y < 0:
        bear_y = -bear_y    #turn positive

    while count < bear_y:
        result = add(result, apple_x)
        count = add(count, 1)

    if x < 0 or y < 0:
        return -result
    return result

def power(x, n):
    """Raise x to power n, where n >= 0"""
    # your code here
    result = 1
    count = 0

    army_x = x
    
    if x < 0:           #if x is negative, make positive
        army_x = -x

    while count < n:
        result = multiply(result,army_x)
        count = add(count,1)

    if n % 2 == 1:      #if power is odd, make result negative
        return -result

    return result


def factorial(x):
    """Compute factorial of x, where x > 0"""
    # your code here
    result = 1
    for bleh in range(1,x+1):
        result = multiply(result, bleh)
    return result


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    # your code here
    blank_list = [0,1]
    
    while len(blank_list) < n:
        total = add(blank_list[-1], blank_list[-2])
        blank_list.append(total)
    result = blank_list[n-1]
    return result


if __name__ == '__main__':
    # your code to call functions above
    print(add(1,2))
    print(multiply(6,-8))
    print(power(-3,5))
    print(factorial(4))
    print(fibonacci(8))