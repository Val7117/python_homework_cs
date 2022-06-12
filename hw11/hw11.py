#!/usr/bin/env python3

# Function letters_range generate a list of letters form first_letter to the last_letter with step.
# Parameters first_letter and last_letter are strongly required, while step is optional (default is 1).

def letters_range(first_letter, last_letter, step=1):
    string = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
    lst = string.split()
    result = []
    for i in list(range(lst.index(first_letter), lst.index(last_letter), step)):
        result.append(lst[i])
    print(result)


print("letters_range('b', 'w', 2)")
letters_range('b', 'w', 2)
print("letters_range('a', 'g')")
letters_range('a', 'g')
print("letters_range('g', 'p')")
letters_range('g', 'p')
print("letters_range('p', 'g', -2)")
letters_range('p', 'g', -2)
print("letters_range('a','a')")
letters_range('a', 'a')
