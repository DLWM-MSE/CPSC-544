from SortAlg.bubble_sort_algoritm import bubble_sort

def test_sorting_silent():
    """ Test sequence sorting in a silent mode
    """
    test_sequence = [1, 3, 5, 3, 2, 2, 7, 1]
    assert bubble_sort(test_sequence, 0, mode="silent") == {'sort_list':[1, 1, 2, 2, 3, 3, 5, 7],\
                                                             'isComplete':True, 'isIteration':True,\
                                                             'swp_ndx':(None, None)}

def test_sorting_verbose():
    """
    Test sequence sorting in 1-step verbose mode
    """
    test_sequence = [4, 3, 2, 1]
    assert bubble_sort(test_sequence, 0, mode="verbose") == {'sort_list':[3, 4, 2, 1],\
                                                             'isComplete':False, 'isIteration':False,\
                                                             'swp_ndx':(0, 1)}
# To run the unit test, run from the containing directory : python -m pytest test_bubble_sort_algoritm.py
