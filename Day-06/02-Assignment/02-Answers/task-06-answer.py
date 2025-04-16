######################################################################################################
# Day-06/02-Assignment/02-Answers/task-06-answer.py
########################################################################################################
# Task 6: Identity and Membership Operators
# 1. Create a list my_list containing a few elements.
# 2. Use identity operators (is and is not) to check if two variables are the same object.
# 3. Use membership operators (in and not in) to check if an element is present in my_list.
# 4. Print the results.

my_list = [10, 20, 30, 40, 50]

a = my_list
b = [10, 20, 30, 40, 50]

# Identity operators
is_same = a is my_list
is_not_same = b is not my_list

# Membership operators
contains_30 = 30 in my_list
not_contains_100 = 100 not in my_list

print("a is my_list:", is_same)
print("b is not my_list:", is_not_same)
print("30 in my_list:", contains_30)
print("100 not in my_list:", not_contains_100)

#########################################################################################################################
### Output:
#########################################################################################################################
@baignashit671 ➜ /workspaces/python-for-devops/python (main) $ python task6.py 
a is my_list: True
b is not my_list: True
30 in my_list: True
100 not in my_list: True
