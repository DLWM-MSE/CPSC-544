def cmd_check(arr):
    """
    Name: cmd_check(arr):
    Input: arr = array of inputs.
    Return: 9 = the user decided to quit the application
            10 = the user decided to start the application again.
    Purpose: Checks the user input on whether they want to quit or continue
    Notes: It is not case sensitive and only
           recongnizes: ['quit', 'q', 'abort', 'stop']|['continue', 'cont']
    """

    quit_cmds = ['quit', 'q', 'abort', 'stop']
    cont_cmds = ['continue', 'cont']
    if isinstance(arr, str):    #this input used after bubble sort it complete
        if arr.lower() in quit_cmds:
            quit()
        elif arr.lower() in cont_cmds:
            return 10
    else:                       #this input used at the start of the bubble sort
        for element in arr:
            if element.lower() in quit_cmds:
                quit()
            elif element.lower() in cont_cmds:
                return 10
