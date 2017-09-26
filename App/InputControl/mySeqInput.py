"""
This function grabs the 2 to 8 user input integer values and returns a sequence of those integers in a list. 
"""

def mySeqInput():
    while True:
        try:
            x = [int(x) for x in input('Please enter 2 to 8 integers below with spaces in between each integer\nInput: ').split()]      #sequences the input into a list
            if len(x) < 2:
                print('more numbers!') 
                break
            elif len(x) > 8:                       
                print('less numbers!')          
                break    
            else:
                return x

        except ValueError:
            print('Integers please!')
            break


#Test code
mySeq = mySeqInput()
