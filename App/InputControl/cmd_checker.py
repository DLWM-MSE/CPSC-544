def cmd_check(arr):
    """
    Name: cmd_check(arr):
    Input: arr = array of inputs.
    Return: 10 = the user decided to start the application again.
    Purpose: Checks the user input on whether they want to quit or continue
    Notes: It is not case sensitive and only
           recongnizes: ['quit', 'q', 'abort', 'stop', 'no']|['continue', 'cont', 'yes']
    """

    quit_cmds = ['quit', 'q', 'abort', 'stop', 'no']
    cont_cmds = ['continue', 'cont', 'yes']
    if isinstance(arr, str):    #this input used after bubble sort it complete
        if arr.lower() in quit_cmds:
            quit()
        elif arr.lower() in cont_cmds:
            return 10
    else:                       #this input used at the start of the bubble sort
        for element in arr:
            if element.lower() in quit_cmds:
                quit()

#----- how to use function -----#
# def main():
#
# while True:
#     mySeq = input()
#     checkQuit = cmd_check(mySeq)
#     #main code
#
#     cmd = input('continue? ')
#     checkQuit = cmd_check(cmd)
#     if checkQuit == 10:
#         continue
