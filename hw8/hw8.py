#!/usr/bin/env python3

# Recursive function which takes entered data and their length as input
# If the last character in string is numeric and data length is more than 0, then
# complete recursive function again and check the character before the last character and repeat.
# Repeat until input string is 'cancel' or one of the other statements are true.

def recursive_check(e_data, l_data):
    if e_data[l_data].isnumeric() and l_data > 0:
        l_data = l_data - 1
        recursive_check(e_data, l_data)
    elif e_data == 'cancel':
        print('Bye!')
        exit(0)
    elif l_data == 0 and e_data.isnumeric() and (int(e_data) % 2 == 0):
        print(int(int(e_data) / 2))
    elif l_data == 0 and e_data.isnumeric() and (int(e_data) % 2 != 0):
        print(int(e_data) * 3 + 1)
    else:
        print('Не удалось преобразовать введенный текст в число.')

# Ask for a prompt until while is True and do the recursive function.
# If the length of entered data is zero then continue the loop.

while 1:
    entered_data = input('-> ')
    if len(entered_data) == 0:
        continue
    last_index = len(entered_data) - 1
    recursive_check(entered_data, last_index)
