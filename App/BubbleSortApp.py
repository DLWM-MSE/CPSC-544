from SortAlg.bubble_sort_algoritm import bubble_sort
from PrintControl.ModPrint import ModPrint


def main():
    """
    Main sequence of the BubbleSortApp. This will act the the controller between
    all modules.
    """
    mySeq = [1, 4, 1, 3, 5, 1, 7, 8, 2, 2, 8, 6]  # <- Test sorting sequence
    #initialize all flags and trackers
    IS_COMPLETE = False
    CUR_NDX = 0
    CUR_ITER = 1

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
            print("{} Swapped @ Indexes {}".format(RTRN_DATAGRAM["sort_list"], RTRN_DATAGRAM["swp_ndx"] ))
            ModPrint.print_yllw_bbl_arr(RTRN_DATAGRAM["sort_list"], RTRN_DATAGRAM["swp_ndx"])
            CUR_NDX = RTRN_DATAGRAM["swp_ndx"][1]   # advance to a next swap index to preserve within-iteration flow

        else:   # isIteration is True and IS_COMPLETE is True -> sorting is complete, do nothing
            pass
    
    print("Sorting is complete!")
if __name__ == "__main__": main()