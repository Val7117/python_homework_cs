#!/usr/bin/env python3

# Fibonacci number generator function, where n is the number of the first n numbers of Fibonacci sequence.
# First IF statement checks, if the entered number n in natural.
# If n == 1 then print 1. If n == 2 then print 1 1. Otherwise, generate numbers and print the result.

def fib(n):
    res = [1, 1]
    string = '1 1'
    if n <= 0:
        print('Incorrect number. Please enter natural number.')
    elif n == 1:
        print("The first number of Fibonacci sequence")
        print('1')
    elif n == 2:
        print("The first 2 numbers of Fibonacci sequence")
        print(string)
    else:
        for i in list(range(1, n - 1)):
            res.append(res[i] + res[i-1])
            string = string + ' ' + str(res[i] + res[i-1])
        print(f"The first {n} numbers of Fibonacci sequence")
        print(string)

fib(20)