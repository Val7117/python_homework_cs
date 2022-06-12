#!/usr/bin/env python3

# Fibonacci number generator function, where n is the number of the n-th element of Fibonacci sequence.
# First IF statement checks, if the entered number n is natural.
# If n == 1 then print the first element of Fibonacci sequence.
# If n == 2 then print the second element of Fibonacci sequence.
# Otherwise, generate the n-th number and print the result.

def fib(n):
    res = [1, 1]
    if n <= 0:
        print('Incorrect number. Please enter natural number.')
    elif n == 1:
        print("The first number of Fibonacci sequence is 1")
    elif n == 2:
        print("The second number of Fibonacci sequence is 1")
    else:
        for i in list(range(1, n - 1)):
            res.append(res[i] + res[i-1])

        print(f"The {n}-th number of Fibonacci sequence is", res[-1])

fib(5432)