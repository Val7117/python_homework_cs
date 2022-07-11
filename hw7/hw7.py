#!/usr/bin/env python3

# Define the range of UIDs to search for [uid_start, uid_end].
uid_start = 1000
uid_end = 10000

# Create empty list, string and two dicts
shells = []
string = ''
uid_gid = dict()        # uid:gid dict
name_uid = dict()       # name:uid dict

# Open "passwd" file for reading and read lines.
# In each line select "shell", remove the sign \n and append to the shell list.
# Also in each line select "name", "UID", "GID" of a user and add to "uid_gid" and "name_uid" dicts.
with open("passwd", "r") as passwd_file:
    lines = passwd_file.readlines()
    for line in lines:
        shell = line.split(":")[-1][:-1]
        shells.append(shell)
        name = line.split(":")[0]
        uid = line.split(":")[2]
        gid = line.split(":")[3]
        uid_gid.update({uid: gid})
        name_uid.update({name: uid})

# Create a dictionary with unique shells
unique_shells = dict.fromkeys(shells)

# For keys (shells) in dictionary count the number of occurrence for each Shell.
# Create a string with the same name and add info from the old string + adding the name of each shell
# and number of its occurrence
for i in unique_shells:
    num = shells.count(i)
    string = string + i + ' - ' + str(num) + ' ; '
string = string[0: -2]      # Get rid of the last space and semicolon '; '


# Create two empty dicts
group_gid_dict = dict()             # group:gid dict
groupName_users = dict()            # group_names: users_in_this_group dict

# Open "group" file for reading and read each line. Get GID, group name, users in this group and
# assign to the correspondent variables. The users' names are split by ',' and resides in a list.
# Add group name and GID to 'group_gid_dict' dict.
# Add group name and users in that group to 'groupName_users' dict.
with open("group", "r") as group_file:
    gr_lines = group_file.readlines()
    for gr_line in gr_lines:
        gr_id = gr_line.split(":")[2]
        gr_name = gr_line.split(":")[0]
        gr_users = gr_line.split(":")[-1][:-1].split(",")
        group_gid_dict.update({gr_name: [gr_id]})
        groupName_users.update({gr_name: gr_users})

# Go through groups (keys) in 'group_gid_dict' and go through UIDs (keys) in 'uid_gid dict'.
# Check and find the correspondent groups and their GIDs, and add to group_gid_dict.
# Here we check for groups of the users in 'passwd' file.
for group in group_gid_dict:
    for uid in uid_gid:
        if uid_gid[uid] in group_gid_dict[group] and uid != group_gid_dict[group][0]:
            group_gid_dict[group].append(uid)

# Here we check 'group' file to get additional permissions.
for gr in groupName_users:
    if len(groupName_users[gr]) > 1:
        for item in groupName_users[gr]:
            group_gid_dict[gr].append(name_uid[item])

# Additional strings for saving the result ('res') and for group checking ('gr_new')
res = ""
gr_new = ""

# Formulate the final result string ('res').
for grName in group_gid_dict:
    for item in group_gid_dict[grName]:
        if (int(item) >= uid_start) and (int(item) <= uid_end) and grName != gr_new:
            res = res + f"{grName}:{item}, "
            gr_new = grName
        elif (int(item) >= uid_start) and (int(item) <= uid_end):
            res = res + f"{item}, "
res = res[:-2]      # Get rid of the last space and comma (', ').

# Write Shells and the number of users, groups and users' UIDs to "output.txt" file.
with open("output.txt", "w") as output:
    output.write(string)
    output.write('\n')
    output.write(res)
    output.write('\n')
