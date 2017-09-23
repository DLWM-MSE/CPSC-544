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
    """ bubble_sort(sort_seq, **kwargs) -> {'sort_list':[],'isComplete':bool, 'isIteration':bool, swp_ndx':(ndx1,ndx2)}"""

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
                    return {'sort_list':sort_seq, 'isComplete':False,'isIteration':False, 'swp_ndx':(i,i + 1)} #pass-out intermediate dort step

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
    #initialize all flags and trackers
    isComplete = False          
    current_index = 0
    current_iteration = 1

    print("Values to be sorted : {}\n".format(mySeq))

#Framework below shows proper use of bubble_sort() function [Run to see the output]:
    while isComplete is False:  # Keep sorting until the entire list is sorted

        return_datagram = bubble_sort(mySeq, current_index, mode = "verbose")    # capture return datagram for futher use

        mySeq = return_datagram["sort_list"]            # capture the current state of sequence under sorting
        isComplete = return_datagram["isComplete"]      # this flag is set True when list can no longer be sorted
        isIteration = return_datagram["isIteration"]    # this flag is set when one complete sorting iteration is complete

        if isIteration is True and isComplete is False:     # advance to a new sorting iteration by resetting swap index to 0
            current_index = 0                               # reset iteration index to start sorting back at index 0
            print("Iteration {} is Complete\n".format(current_iteration))
            current_iteration += 1

        elif isIteration is False and isComplete is False:
            print("{} Swapped @ Indexes {}".format(return_datagram["sort_list"], return_datagram["swp_ndx"] ))
            current_index = return_datagram["swp_ndx"][1]   # advance to a next swap index to preserve within-iteration flow

        else:   # isIteration is True and isComplete is True -> sorting is complete, do nothing
            pass
    
    print("Sorting is complete!")