def cmd_check(arr):
    """
    Name: cmd_check(arr):
    Input: arr = array of inputs.
    Return: 'cont' = the user decided to start the application again.
            'quit' = the user wants to end the application.
            1 = error.
    Purpose: Checks the user input on whether they want to quit or continue
    Notes: It is not case sensitive and only
           recongnizes: ['quit', 'q', 'abort', 'stop', 'no']|['continue', 'cont', 'yes']
    """

    quit_cmds = ['quit', 'q', 'abort', 'stop', 'no']
    cont_cmds = ['continue', 'cont', 'yes']
    verb_cmds = ['verbose', 'v']
    slnt_cmds = ['silent', 's']
    if isinstance(arr, str):    #this input used after bubble sort it complete
        if arr.lower() in quit_cmds:
            return 'quit'
        elif arr.lower() in cont_cmds:
            return 'cont'
        elif arr.lower() in verb_cmds:
            return 'verbose'
        elif arr.lower() in slnt_cmds:
            return 'silent'
        else:
            return 1
    else:                       #this input used at the start of the bubble sort
        for element in arr:
            if element.lower() in quit_cmds:
                return 'quit'
            else:
                return 1

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
