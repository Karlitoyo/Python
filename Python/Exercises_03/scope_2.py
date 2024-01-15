# Define a function that takes two arguments: a list and an integer.
def find_num(number_list: list, number: int)->bool:
    # Iterate through each element in the list
    for iterate_number in number_list:
        # Check if iterate_number is equal to the number.
        if iterate_number == number:
            # if equal return true
            return True
        else:
            # if not continue iterating
            pass

# Call the 'find_num' function with a list 1-8 and the number 9.
result = find_num([1,2,3,4,5,6,7,8], 9)
# Print the result
print(result)

# Define a function that takes two arguments: a list and an integer.
def find_num(number_list: list, number: int)->bool:
    # Iterate through each element in the list
    for iterate_number in number_list:
        # Check if iterate_number is equal to the number.
        if iterate_number == number:
            # if equal return true
            return True
        # updated code to return false
    return False

# Call the 'find_num' function with a list 1-8 and the number 9.
result = find_num([1,2,3,4,5,6,7,8], 9)
# Print the result
print(result)