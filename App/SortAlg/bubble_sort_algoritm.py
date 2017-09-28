"""
This module performs Bubble Sort algorithm on a series of integer values
to sort the numbers in the ascending order

Inputs: bubble_sort(sort_seq, sort_index [,mode = "verbose"])
            sort_seq<list> specifies the sequence to be sorted
            sort_index<int> keeps track of sorting iterative index. Neessary only in "verbose" mode
            mode<dict> specifies notification behavior : "verbose" or "silent"
                "verbose" (default) outputs EVERY sorting step
                "silent" outputs ONLY the final sorted sequence

Return:     [seq_sort]<list>, - partially or fully sorted list of values
            isComplete<bool>, - flag that indicates that returned list is fully sorted
            isIteration<bool>,- flag that indicates that sequence one full iteration is finished
            swp_ndx<tuple> - location of swapped list indexes (seq_sort[ndx1],seq_sort[ndx2]). If nothing swapped, tuple is (None, None)

Flag Notes: isComplete == True and isIteration ==True -> the sequence is completely sorted
    isComplete == False and isIteration == True -> the sorting iteration is complete BUT sequence can be sorted furter
    isComplete == False amd isIteration == False -> intermediate sorting step within a given iteration.
                                                    Sorting is neither complete not it is yet rached a complete iteration
"""
def bubble_sort(sort_seq, start_index, **kwargs):
    """ bubble_sort(sort_seq, sort_index, **kwargs) ->
    {'sort_list':[],'isComplete':bool, 'isIteration':bool, swp_ndx':(ndx1,ndx2)}
    """

    sort_mode = kwargs.get('mode', "verbose")   #if mode is not passed, default to "verbose"
    num_elements = len(sort_seq) # Get the total number of sequence elements in sorting sequence

    if sort_mode is not "verbose":
        # "silent" mode sorts the entire sequence without intermediate steps
        # and returns fully-sorted final list of values

        swapped = True                  # Initialize swap tracker to enter the while-loop
        while swapped is True:
            swapped = False             # Reset swap-tracker
            for i in reversed(range(1, num_elements)):

                if sort_seq[i] < sort_seq[i - 1]:
                    # Swap adjacent values
                    sort_seq[i], sort_seq[i - 1] = sort_seq[i - 1], sort_seq[i]
                    swapped = True

        FLG_COMPLETE = True
        FLG_ITERATION = True
        SWAP_INDEX = (None, None)

        return {'sort_list':sort_seq, 'isComplete':FLG_COMPLETE, 'isIteration':FLG_ITERATION, 'swp_ndx':SWAP_INDEX}
    else:
        # "verbose" mode : returns sequence as it propagates through every sorting step.
        # Returned datagram also contains important flags about the state of the sorting
        swapped = False
        for i in reversed(range(1, start_index + 1)):

            if sort_seq[i] < sort_seq[i - 1]:
                sort_seq[i], sort_seq[i - 1] = sort_seq[i - 1], sort_seq[i] # Swap adjacent values
                swapped = True
                #pass-out intermediate sort step and appropriate flags
                return {'sort_list':sort_seq, 'isComplete':False, 'isIteration':False, 'swp_ndx':(i, i - 1)}

        if swapped is False and start_index is len(sort_seq) - 1:
            # sorting is complete since no swaps occured as we went from index 0 to the end
            FLG_COMPLETE = True
            FLG_ITERATION = True
            SWAP_INDEX = (None, None)
        else:
            # One Iteration is compete but sorting is not yet Complete
            FLG_COMPLETE = False
            FLG_ITERATION = True
            SWAP_INDEX = (None, None)

        return {'sort_list':sort_seq, 'isComplete':FLG_COMPLETE, 'isIteration':FLG_ITERATION, 'swp_ndx':SWAP_INDEX}

if __name__ == "__main__": # Execute this <tester code> is the module clled as a top-level script

    mySeq = [9, 8, 3, 2, 4, 6, 1]  # <- Test sorting sequence
    #initialize all flags and trackers
    IS_COMPLETE = False
    CUR_NDX = len(mySeq) - 1  #Start at the last element of the passes list
    CUR_ITER = 1

    print("Values to be sorted : {}\n".format(mySeq))

# ==== Framework below shows proper use of bubble_sort() function [Run to see the output]: ====

    while IS_COMPLETE is False:  # Keep sorting until the entire list is sorted

        RTRN_DATAGRAM = bubble_sort(mySeq, CUR_NDX, mode = "verbose")    # capture return datagram for futher use

        mySeq = RTRN_DATAGRAM["sort_list"]            # capture the current state of sequence under sorting
        IS_COMPLETE = RTRN_DATAGRAM["isComplete"]      # this flag is set True when list can no longer be sorted
        isIteration = RTRN_DATAGRAM["isIteration"]    # this flag is set when one complete sorting iteration is complete

        if isIteration is True and IS_COMPLETE is False:     # advance to a new sorting iteration by resetting swap index to last element
            CUR_NDX = len(mySeq) - 1                               # reset iteration index to start sorting back at index of last element
            print("Iteration {} is Complete\n".format(CUR_ITER))
            CUR_ITER += 1

        elif isIteration is False and IS_COMPLETE is False:
            print("{} Swapped @ Indexes {}".format(RTRN_DATAGRAM["sort_list"], RTRN_DATAGRAM["swp_ndx"] ))
            CUR_NDX = RTRN_DATAGRAM["swp_ndx"][0]   # advance to a next swap index to preserve within-iteration flow

        else:   # isIteration is True and IS_COMPLETE is True -> sorting is complete, do nothing
            pass
    
    print("Sorting is complete!")
    print(mySeq)