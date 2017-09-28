from colorama import init, Fore, Back, Style
from SortAlg.bubble_sort_algoritm import bubble_sort
from PrintControl.ModPrint import ModPrint
from InputControl.input_checker import input_check
from InputControl.cmd_checker import cmd_check
from ErrorReporter.ErrorReporter import ErrorReport



def main():

    """
    Main sequence of the BubbleSortApp. This will act the the controller between
    all modules.
    """
    
    while True:
        #initialize all flags and trackers
        IS_COMPLETE = False
        CUR_NDX = 0
        CUR_ITER = 1
        
        init()
        while True:

            mySeq = input("Please enter 2 to 8 single digit integer below with spaces in between each value.\n"\
                          "Or enter 'quit', 'q', 'abort', 'stop', or 'no' to end the application.\n"\
                          "Input: ").split()
            outputError = False # Error output control

            inputCheckResult = input_check(mySeq) # Check if input is for sorting
            cmdCheckResult = cmd_check(mySeq) # Check if input is a command
         
            if inputCheckResult != 0 and cmdCheckResult == 'quit': # Input is a quit command
                quit() # Quit the program
            elif cmdCheckResult == 1 and inputCheckResult == 0: # Input is meant to be sorted
                outputError = 0
            elif inputCheckResult and cmdCheckResult: # Input is not recognized as either values to be sorted or a command
                outputError = True

            if outputError: # If the input is neither values to be sorted or a command
                ModPrint.print_red("Error: ")
                ModPrint.print_red(ErrorReport.define_error_code('ValInput', inputCheckResult))
                ModPrint.print_red("OR")
                ModPrint.print_red(ErrorReport.define_error_code('StrtCmdInput', cmdCheckResult))
            else: # No errors found
                ModPrint.print_yellow("Inputs Accepted!")
                mySeq = [int(i) for i in mySeq]
                break

        print("Values to be sorted : {}\n".format(mySeq))
    # ==== Framework below shows proper use of bubble_sort() function [Run to see the output]: ====

        while IS_COMPLETE is False:  # Keep sorting until the entire list is sorted

            RTRN_DATAGRAM = bubble_sort(mySeq, CUR_NDX, mode = "verbose")    # capture return datagram for futher use

            mySeq = RTRN_DATAGRAM["sort_list"]            # capture the current state of sequence under sorting
            IS_COMPLETE = RTRN_DATAGRAM["isComplete"]      # this flag is set True when list can no longer be sorted
            isIteration = RTRN_DATAGRAM["isIteration"]    # this flag is set when one complete sorting iteration is complete

            if isIteration is True and IS_COMPLETE is False:     # advance to a new sorting iteration by resetting swap index to 0
                CUR_NDX = 0                               # reset iteration index to start sorting back at index 0
                print("Iteration {} is Complete\n".format(CUR_ITER))
                CUR_ITER += 1

            elif isIteration is False and IS_COMPLETE is False:
                #print("{} Swapped @ Indexes {}".format(RTRN_DATAGRAM["sort_list"], RTRN_DATAGRAM["swp_ndx"] ))
                ModPrint.print_yllw_bbl_arr(RTRN_DATAGRAM["sort_list"], RTRN_DATAGRAM["swp_ndx"])
                CUR_NDX = RTRN_DATAGRAM["swp_ndx"][1]   # advance to a next swap index to preserve within-iteration flow

            else:   # isIteration is True and IS_COMPLETE is True -> sorting is complete, do nothing
                pass

        print("Sorting is complete!")
        while True:
            cmd = input("To continue, enter: 'continue', 'cont', or 'yes'\n"\
                        "To quit, enter: 'quit', 'q', 'abort', 'stop', or 'no'\n"\
                        "Input: ") # Asks user for input
            cmdCheckResult = cmd_check(cmd) # Checks input
            if cmdCheckResult == 'cont': # If continue, break out of this loop
                break
            elif cmdCheckResult == 'quit': # If quit, end the application
                quit()
            elif cmdCheckResult == 1: # If error, stay in the loop to ask froma proper input
                ModPrint.print_red("Error: ")
                ModPrint.print_red(ErrorReport.define_error_code('IntrCmdInput', cmdCheckResult))

if __name__ == "__main__": main()
