# Task 5: Bitwise Operators (Optional)
# 1. If you are comfortable with bitwise operators, perform some bitwise operations on integer values and print the results. 
# If not, you can skip this task.

my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

is_same_object = a is my_list
is_not_same_object = b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)
