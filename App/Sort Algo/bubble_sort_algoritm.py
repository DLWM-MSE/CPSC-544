"""
This module performs Bubble Sort algorithm on a series of integer values
to sort the numbers in the ascending order

Inputs: bubble_sort(sort_seq[,mode = "verbose", speed = "0.5"])
            mode specifies notification behavior : "verbose" or "silent"
                "verbose" (default) outputs EVERY sorting step
                "silent" outputs ONLY the final sorted sequence

            speed specifies an output delay between each sorting step
                float(speed) has a default value of "0.7" seconds

Outputs: None

"""
from time import sleep

def bubble_sort(sort_seq, **kwargs):

    sort_mode = kwargs.get('mode', "verbose")
    sort_speed = float(kwargs.get('speed',"0.5"))
    num_elements = len(sort_seq)       # Get the total number of sequence elements in sorting sequence
    swapped = True                  # Initialize swap tracker to enter the while-loop

    while swapped == True:
        swapped = False             # Reset swap-tracker
        for i in range(num_elements - 1):

            if sort_seq[i] > sort_seq[i + 1]:
                sort_seq[i],sort_seq[i + 1] = sort_seq[i + 1],sort_seq[i] # Swap adjacent values
                swapped = True

                if sort_mode == "verbose": # verbose mode assures display of all sorting steps
                    print(sort_seq)
                    sleep(sort_speed)

    print("Sorting is Complete: {}".format(sort_seq))

if __name__ == "__main__": # Execute this <tester code> is the module clled as a top-level script

    help(bubble_sort)
    bubble_sort([9, 9, 1, 4, 5, 2, 6], mode = "verbose", speed = "1.5")