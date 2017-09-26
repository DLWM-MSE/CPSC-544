"""
This function grabs the 2 to 8 user input integer values and returns a sequence of those integers in a list.
"""

def mySeqInput():
    try:
        x = [int(x) for x in input('Please enter 2 to 8 integers below with spaces in between each integer\nInput: ').split()]      #sequences the input into a list
        for i in x:
            if not 1 <= i <= 9:
                print('single digits only!')
                break
        if len(x) < 2:
            print('more numbers!')
        elif len(x) > 8:
            print('less numbers!')

        else:
            print(x)

    except ValueError:                  #Haven't figured out how to output regarding float inputs.
        print('Integers please!')       #This is why I have the while/try/except loop.

#Test code
mySeq = mySeqInput()
