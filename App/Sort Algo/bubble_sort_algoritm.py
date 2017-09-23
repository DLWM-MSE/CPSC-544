"""
This module performs Bubble Sort algorithm on a series of integer values
to sort the numbers in the ascending order

Inputs: bubble_sort(sort_seq[,mode = "verbose"])
            mode specifies notification behavior : "verbose" or "silent"
                "verbose" (default) outputs EVERY sorting step
                "silent" outputs ONLY the final sorted sequence

Return:     [seq_sort]<list>, - partially or fully sorted list of values
            isComplete<bool>, - flag that indicates that returned list is fully sorted
            swp_ndx<tuple> - location of swapped list indexes (seq_sort[ndx1],seq_sort[ndx2])
"""
def bubble_sort(sort_seq, start_index, **kwargs):
    """ bubble_sort(sort_seq, **kwargs) -> {'sort_list':[],'isComplete':bool,'swp_ndx':(ndx1,ndx2)}"""
    sort_mode = kwargs.get('mode', "verbose")   #if mode is not passed, default to "verbose"
    num_elements = len(sort_seq)                # Get the total number of sequence elements in sorting sequence

    if sort_mode is not "verbose":      
        # "silent" mode sorts the entire sequence without intermediate steps
        # and returns fully-sorted final list of values

        swapped = True                  # Initialize swap tracker to enter the while-loop
        while swapped is True:
            swapped = False             # Reset swap-tracker
            for i in range(num_elements - 1):

                if sort_seq[i] > sort_seq[i + 1]:
                    sort_seq[i],sort_seq[i + 1] = sort_seq[i + 1],sort_seq[i] # Swap adjacent values
                    swapped = True

        flgComplete = True
        flgIteration = True
        SwapIndex = (None,None)

        return {'sort_list':sort_seq, 'isComplete':flgComplete, 'isIteration':flgIteration, 'swp_ndx':SwapIndex}
        
    else:
        # "verbose" mode ...
        swapped = False  
        for i in range(start_index, num_elements - 1):

                if sort_seq[i] > sort_seq[i + 1]:
                    sort_seq[i],sort_seq[i + 1] = sort_seq[i + 1],sort_seq[i] # Swap adjacent values
                    swapped = True
                    return {'sort_list':sort_seq, 'isComplete':False,'isIteration':False, 'swp_ndx':(i,i + 1)}

        if swapped is False and start_index is 0:
            flgComplete = True
            flgIteration = True
            SwapIndex = (None,None)
        else:
            flgComplete = False
            flgIteration = True
            SwapIndex = (None,None)

        return {'sort_list':sort_seq, 'isComplete':flgComplete,'isIteration':flgIteration, 'swp_ndx':SwapIndex}  

    



if __name__ == "__main__": # Execute this <tester code> is the module clled as a top-level script

    mySeq = [1, 4, 1, 3, 5, 1]  # <- Test sorting sequence
    isComplete = False
    current_index = 0
    current_iteration = 1
    print("Values to be sorted : {}\n".format(mySeq))

#Framework that shows proper use of bubble_sort() function :
    while isComplete is False:  # Keep sorting until the entire list is sorted

        return_datagram = bubble_sort(mySeq, current_index, mode = "verbose")    # capture return datagram for futher use

        isComplete = return_datagram["isComplete"]      # this flag is set True when list can no longer be sorted
        isIteration = return_datagram["isIteration"]    # this flag is set when one complete sorting iteration is complete

        if isIteration is True and isComplete is False:     # advance to a new sorting iteration by resetting swap index to 0
            current_index = 0
            print("Iteration {} is Complete\n".format(current_iteration))
            current_iteration += 1

        elif isIteration is False and isComplete is False:
            print("{} Swapped @ Indexes {}".format(return_datagram["sort_list"], return_datagram["swp_ndx"] ))
            current_index = return_datagram["swp_ndx"][1]   # advance to a next swap index to preserve within-iteration flow

        else:
            pass
    
    print("Sorting is complete!")