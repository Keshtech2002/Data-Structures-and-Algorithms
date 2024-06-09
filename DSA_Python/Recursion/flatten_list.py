# A recursive function to flatte a nested list structure

def flatten_list(nested_list):
    # Initialize list to contain the result
    result_list =[]
    # Iterate through initial list
    for item in nested_list:
        # Check if item in the list is a list
        if isinstance(item, list):
            # If it is a list, recursively call the function
            # extend() is used to add elements of an iterable 
            # (such as string, list, tuple, set, etc.) to the 
            # end of another list 
        # if type(item) is list:
            result_list.extend(flatten_list(item))
        else:
            result_list.append(item)
    return result_list


nested_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten_list(nested_list))

# # Notes
# Using append()
# my_list.append ([6, 0, 4, 1])
# print (my_list)
# >>> ['geeks', 'for', 'geeks', [6, 0, 4, 1]]

# Using extend()
# my_list.extend([6, 0, 4, 1])
# print (my_list)
# >>> ['geeks', 'for', 'geeks', 6, 0, 4, 1]