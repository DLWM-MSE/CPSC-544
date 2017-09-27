"""
This module contains the Class ErrorReport. This class does not need to be
instantiated given that all methods are defined to be static.
"""
class ErrorReport:
    """
    A simple error reporter class
    """
    #ATTRIBUTES
    __errorCodes = {'ValInput': {0: "No error",
                                 1: "Error: an input was less than 0 and/or greater than 9",
                                 2: "Error: the number of inputs are less than 2",
                                 3: "Error: the number of inputs are greater than 8",
                                 4: "Error: there is an input that is not an integer"},
                    'CmdInput': {0: "No error",
                                 1: "Error: Can either enter QUIT or values to be sorted"}}

    #METHODS
    @classmethod
    def get_error(cls, errorType, code):
        """
        Name: classmethod get_error(errorType, code)
        Input: errorType<string> = library of error codes to be checked.
                                   Current Libraries: 'ValInput': input_checker errors.
                                                      'CmdInput': command_checker errors.
               code<int> = error code.
        Return: Upon success, proper error message is returned, otherwise lets user
                know that the error library or error code is not defined.
        Purpose: To return error messages corresponding to the error code.
        Notes: Return example: "Error: an input was less than 0 and/or greater than 9"
        """
        if errorType in cls.__errorCodes:
            if code in cls.__errorCodes[errorType]:
                return cls.__errorCodes[errorType][code]
            else:
                return "ERROR: Error code " + str(code) + " is not defined in the Input error library!"
        else:
            return "ERROR: Error type does not exist!"
    @staticmethod
    def define_error_code(errorType, code):
        """
        Name: staticmethod define_error_code(errorType, code):
        Input: errorType<string> = library of error codes to be checked.
               code<int> = error code.
        Return: Upon success, proper error message is returned, otherwise lets user
                know that the error library or error code is not defined.
        Purpose: Calls the class member method get_error to access the private error library.
        Notes: Return example: "Error: an input was less than 0 and/or greater than 9"
        """
        return ErrorReport.get_error(errorType, code)
