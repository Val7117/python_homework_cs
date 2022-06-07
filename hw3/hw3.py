#!/usr/bin/env python3

# In Python 1 is always gives True in boolean

while 1:

# Taking an input

    input_data = input('-> ')

# Making unique text (lower case) and splitting it

    lower_text = input_data.lower()
    formatted_data =  lower_text.split() 

# Empty list for popular words and starting number for checking

    popular_words = []
    max_num = 0

# Main algorithm. Count the number of occurence for each entered word. 
# If count is more than max_num then this is the most popular word and the max_num changes its value
# If count is the same as max_num then append this word.
# Otherwise continue the cycle for

    for i in formatted_data:
        repeatitions = formatted_data.count(i)
        if repeatitions > max_num:
            popular_words = [i]
            max_num = repeatitions
        elif repeatitions == max_num and i not in popular_words:
            popular_words.append(i)
        else:
            continue

# Printing popular words and number of their appearance

    for j in popular_words:
        print(max_num,' - ', j)
    
    print('')
