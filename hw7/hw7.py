#!/usr/bin/env python3

# Create empty list, string and dict

shells = []
string = ''
uids = dict()

# Open "passwd" file for reading and read lines.
# In each line select "shell", remove the sign \n and append to the shell list.
# Also in each line select "name" and "UID" of a user and add to "uids" dictionary

with open("passwd", "r") as passwd_file:
    lines = passwd_file.readlines()
    for line in lines:
        shells.append(line.split(":")[-1][:-1])
        name = line.split(":")[0]
        uid = line.split(":")[2]
        uids.update({name: uid})

# Create a dictionary with unique shells

unique_shells = dict.fromkeys(shells)

# For keys (shells) in dictionary count the number of occurrence for each shell
# Create a string with the same name and add info from the old string + adding the name of a each shell
# and number of its occurrence

for i in unique_shells:
    num = shells.count(i)
    string = string + i + ' - ' + str(num) + ' ; '

# Create an empty group_dict

group_dict = dict()

# Open "group" file for reading and read each line. Get the username (or names if there is more than one)
# and assign the value(values) to variable "user_name". Get the group name and assign the value to the variable
# called "group_name". Both  "user_name" and "group_name" add to group_dict.

with open("group", "r") as group_file:
    gr_lines = group_file.readlines()
    for gr_line in gr_lines:
        if gr_line.split(":")[-1][:-1]:
            user_name = gr_line.split(":")[-1][:-1]
            user_name = user_name.split(',')
            group_name = gr_line.split(":")[0]
            group_dict.update({group_name: user_name})

# Create and empty additional strings for the result and group

res = ''
gr = ''

# Go through group_dict.keys and group_dict values and create a new string adding the old 'res' string and
# a new pair of group's name and users' UIDs.
# There is also an additional check for the right output. If the previous group's name is the same as current,
# then only add ',' and user's UID. Otherwise add group's name and user's UID.

for group in group_dict.keys():
    gr_new = group
    for i in group_dict[group]:
        if gr_new == gr:
            res = res + ',' + f'{uids[i]}'
        else:
            res = res + f'{group}' + ':' + f'{uids[i]}'
            gr = gr_new
    res = res + " "

# Write shells and the number of users, groups and users' UIDs to "output.txt" file.

with open("output.txt", "w") as output:
    output.write(string)
    output.write('\n')
    output.write(res)
