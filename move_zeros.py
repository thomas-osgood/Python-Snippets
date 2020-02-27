#!/usr/bin/python3

"""
    Function to move ZEROs to the back of an 
    array.
    
    Ex:
    [a,0,1,1,3,0,5] ==> [a,1,1,3,5,0,0]
"""

def move_zeros(array):
    i = 0
    c = []
    z = []
    
    """
    Walk Through Array And Check For Zero.
    If ZERO, add to ZERO Array, otherwise
    add to other array.
    """
    for i in range(len(array)):
        if ((array[i] == 0) and not(array[i] is False)):
            z.append(array[i])
        else:
            c.append(array[i])
    
    """
    Concat Two Arrays
    """
    c += z
    
    return c
