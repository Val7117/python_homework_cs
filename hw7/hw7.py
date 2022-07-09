#!/usr/bin/env python3

# Define the range of UID to search for [uid_start, uid_end].
uid_start = 1000
uid_end = 10000

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
# Create a string with the same name and add info from the old string + adding the name of each shell
# and number of its occurrence

for i in unique_shells:
    num = shells.count(i)
    string = string + i + ' - ' + str(num) + ' ; '
string = string[0: -3]      # Get rid of the last space and semicolon '; '
# Create an empty group_dict

group_dict = dict()

# Open "group" file for reading and read each line. Get the username (or names if there is more than one)
# and assign the value(values) to variable "user_name". Get the group name and assign the value to the variable
# called "group_name". Both  "user_name" and "group_name" add to group_dict.

with open("group", "r") as group_file:
    gr_lines = group_file.readlines()
    for gr_line in gr_lines:
        user_name = gr_line.split(":")[-1][:-1]
        user_name = user_name.split(',')
        group_name = gr_line.split(":")[0]
        group_dict.update({group_name: user_name})

# Create empty additional strings for the result and group
res = ''
gr = ''
# Create empty dictionary for user's UIDs.
users_uids = dict()

# Select the needed UIDs from 'uids' dictionary and always search for the 'root'.
for uid in uids:
    if uid == 'root' or (uid_start <= int(uids[uid]) <= uid_end):
        users_uids.update({uid: uids[uid]})

# Collect needed groups and UIDs and create the resulting string.
for group in group_dict:
    for uid in users_uids:
        if uid in group_dict[group] or uid == group:
            if group == gr:
                res = res + f"{users_uids[uid]}, "
            else:
                res = res + f"{group}:" + f"{users_uids[uid]}, "
                gr = group
res = res[0:-2]     # Get rid of the last comma in the string.

# Write shells and the number of users, groups and users' UIDs to "output.txt" file.
with open("output.txt", "w") as output:
    output.write(string)
    output.write('\n')
    output.write('\n')
    output.write(res)
    output.write('\n')
