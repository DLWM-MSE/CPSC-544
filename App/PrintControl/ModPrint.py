"""
This module contains the Class ModPrint. This class does not need to be
instantiated given that all methods are defined to be static.
"""
class ModPrint:
    """A simple text printer that applies style modifier
    """
    #ATTRIBUTES

    #Attributes for text modifiers
    boldMod = "\033[1m"
    endMod = "\033[0m"
    redMod = "\033[1;31;40m"
    yellowMod = "\033[1;33;40m"


    #METHODS  
    @staticmethod
    def bold(msg):
        """
        Name: staticmethod bold(msg)
        Input: msg = message to be turned bold
        Return: msg with added bold modifiers
        Purpose: add bold modifiers to input message
        Notes: Return example: '\033[1m' + msg + '\033[0m'
        """
        return ModPrint.boldMod + msg + ModPrint.endMod

    @staticmethod
    def print_bold(msg):
        """
        staticmethod print_bold(msg)
        Input: msg = message to be printed bold
        Output: NONE
        Purpose: print input message bold
        Notes:
        """
        print(ModPrint.bold(msg))

    @staticmethod
    def print_bold_bbl_arr(arr, loc):
        """
        staticmethod print_bold_bbl_arr(arr,loc)
        Input: arr = array of integers to be printed,
               loc = two locations to be printed bold
        Output: NONE
        Purpose: Print two specific values out of an array of integers bold.
                 A space in between the arrays will be added.
        Notes:
        """
        for index in range(len(arr)): 
            if index == loc[0] or index == loc[1]:
                print(ModPrint.bold(str(arr[index])), end=" ")
            else:
                print(arr[index], end=" ")
        print("")

    @staticmethod
    def red(msg):
        """
        staticmethod Red(msg)
        Input: msg = message to be turned red
        Return: msg with added red modifiers
        Purpose: add red modifiers to input message
        Notes: Return example: '\033[1;31;40m' + msg + '\033[0m'
        """
        return ModPrint.redMod + msg + ModPrint.endMod

    @staticmethod
    def print_red(msg):
        """
        staticmethod print_red(msg)
        Input: msg = message to be printed red
        Output: NONE
        Purpose: print input message red
        Notes:
        """
        print(ModPrint.red(msg))
    
    @staticmethod
    def yellow(msg):
        """
        staticmethod yellow(msg)
        Input: msg = message to be turned yellow
        Return: msg with added yellow modifiers
        Purpose: add red modifiers to input message
        Notes: Return example: '\033[1;31;40m' + msg + '\033[0m'
        """
        return ModPrint.yellowMod + msg + ModPrint.endMod

    @staticmethod
    def print_yellow(msg):
        """
        staticmethod print_yellow(msg)
        Input: msg = message to be printed yellow
        Output: NONE
        Purpose: print input message yellow
        Notes:
        """
        print(ModPrint.yellow(msg))

    @staticmethod
    def print_yllw_bbl_arr(arr, loc):
        """
        staticmethod print_yllw_bbl_arr(arr,loc)
        Input: arr = array of integers to be printed, loc = two locations to be printed yellow
        Output: NONE
        Purpose: Print two specific values out of an array of integers bold.
                 A space in between the arrays will be added.
        Notes:
        """
        for index in range(len(arr)): 
            if index == loc[0] or index == loc[1]:
                print(ModPrint.yellow(str(arr[index])), end=" ")
            else:
                print(arr[index], end=" ")
        print("") 