def cmd_check(arr):
    """
    Name: cmd_check(arr):
    Input: arr = array of inputs.
    Return: 9 = the user has decided to quit the application
    Purpose: Checks the user input on whether they want to quit.
    Notes: It is not case sensitive and only
           recongnizes: ['quit', 'q', 'abort', 'stop'].
    """

quit_cmds = ['quit', 'q', 'abort', 'stop']
    for element in arr:
        if element.lower() in quit_cmds:
            return 9
