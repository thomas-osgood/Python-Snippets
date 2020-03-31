#!/usr/bin/python3
"""
data and data1 are two strings with rainfall records of a few cities for months from January to December. The records of towns are separated by \n. The name of each town is followed by :.

data and towns can be seen in "Your Test Cases:".
Task:

    function: mean(town, strng) should return the average of rainfall for the city town and the strng data or data1 (In R and Julia this function is called avg).
    function: variance(town, strng) should return the variance of rainfall for the city town and the strng data or data1.

Examples:

mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)

Notes:

    if functions mean or variance have as parameter town a city which has no records return -1 or -1.0 (depending on the language)

    Don't truncate or round: the tests will pass if abs(your_result - test_result) <= 1e-2 or abs((your_result - test_result) / test_result) <= 1e-6 depending on the language.

    Shell tests only variance

    A ref: http://www.mathsisfun.com/data/standard-deviation.html

    data and data1 (can be named d0 and d1 depending on the language; see "Sample Tests:") are adapted from: http://www.worldclimate.com
"""

def mean(town, strng):
    """
    Function Name: mean
    Input(s):
        town - town name.
        strng - data string
    Description:
        Return the mean of a town given
        a data string.
    """
    t_data = strng.split('\n')
    d_dict = {}
    retVal = 0
    i = 0
    
    for l in t_data:
        avg = 0
        t = l.split(':')[0]
        mos = l.split(':')[1].split(',')
        for dp in mos:
            n = dp.split(' ')[1]
            avg += float(n)
        avg /= 12
        d_dict[t] = avg
        i += 1
    
    if town in d_dict:
        retVal = d_dict[town]
    else:
        retVal = -1
    
    return retVal
    
def variance(town, strng):
    """
    Function Name: variance
    Input(s):
        town - town name.
        strng - data string
    Description:
        Return the variance of a town's data given
        a data string.
    """
    t_data = strng.split('\n')
    m = mean(town, strng)
    d_dict = {}
    retVal = 0
    
    if (m < 0):
        return -1
        
    for l in t_data:
        t = l.split(':')[0]
        mos = l.split(':')[1].split(',')
        mos_avg = 0
        dif = 0
        avg = 0
        for dp in mos:
            n = float(dp.split(' ')[1])
            dif = m - n
            avg += (dif ** 2)
        d_dict[t] = avg

    if town in d_dict:
        retVal = d_dict[town] / 12
    else:
        retVal = -1
    
    return retVal
