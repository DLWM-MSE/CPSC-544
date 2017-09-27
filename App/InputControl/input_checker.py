"""
This function grabs the 2 to 8 user input integer values and returns a sequence of those
integers in a list.
"""
def input_check(arr):
    """
    Name: input_check(arr):
    Input: arr = array of inputs.
    Return: 0 = no error
            1 = a number is less than 1 or greater than 9.
            2 = the input size is less than 2.
            3 = the input size is greater than 8.
            4 = the input is not an integer.
    Purpose: Check array input.
    Notes: Values must be integers between 1 and 9, and the number of values must be
           2 and 8.
    """

    for num in arr:
        match = any(c.isalpha() for c in num) #Search for alphabets.
        if match:
            return 4 #Error: input is not an integer.
        match = num.find('.') #Search for doubles.
        if match >= 0:
            return 4 #Error: input is not an integer.
        if not 0 <= int(num) <= 9:
            return 1 #Error: A number is less than 1 or greater than 9.
    if len(arr) < 2:
        return 2 #Error: The number of inputs are less than 2.
    elif len(arr) > 8:
        return 3 #Error: The number of inputs are greater than 8.
    else:
        return 0 #No Error.
