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

    while True:

        mySeq = input('Please enter 2 to 8 single digit integers below with spaces in between each value\nInput: ').split()
        checkResult = input_check(mySeq) # Acquire result of input check
        checkQuit = cmd_check(mySeq)

        if checkResult: # If the result is anything but 0
            ModPrint.print_red(ErrorReport.define_error_code('ValInput', checkResult))
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
    cmd = input('continue? ')
    checkQuit = cmd_check(cmd)
    if checkQuit == 10:
        continue

if __name__ == "__main__": main()
