#!/usr/bin/python3
"""
    Check Interesting Car Mile Numbers
    
    Main Function is "is_interesting".
    
    Returns 2 If:
        - number is all the same digit (ie: 111111)
        - number is palindrome
        - number is incrementing (ie: 7890)
        - number is decrementing (ie: 3210)
        - number has one digit and the rest zeros (ie: 10000)
        - number is one of the numbers in awesome_phrases array/list.
    
    Returns 1 If There Is An Interesting Number Within Two Miles And The Current
    Number Is Not Interesting.
    
    Returns 0 If The Current Number Is Not Interesting And An Interesting Number
    Does Not Occur Within Two Miles.
"""

def is_palindrome(number):
    retVal = False
    
    # Convert Number To String For Manipulation
    snum = str(number)
    
    # Reverse String For Comparison
    revnum = snum[::-1]
    
    # Compare Two Strings. If Same, Return Value Is True
    if (snum == revnum):
        retVal = True
    
    return retVal

def is_interesting(number, awesome_phrases):
    # Init Local Variables
    number1 = number + 1
    number2 = number + 2
    snum = str(number)
    snum1 = str(number1)
    snum2 = str(number2)
    nlen = len(snum)
    nlen1 = len(snum1)
    nlen2 = len(snum2)
    inc_str = '1234567890'
    dec_str = '9876543210'
      
    # Check If Interesting Number Now
    if (nlen > 2):
        # Check For All Zeros After First Number
        if (snum[1:].count('0') == len(snum[1:])):
            return 2
        
        # Check For All Numbers The Same
        if (snum.count(snum[0]) == len(snum)):
            return 2
            
        # Check For Incrementing Number
        if (snum in inc_str):
            return 2
            
        # Checkk For Decrementing Number
        if (snum in dec_str):
            return 2
        
        # Check For Palindrome
        if (is_palindrome(number) == True):
            return 2
            
        # Check Awesome_Phrases Array
        if (number in awesome_phrases):
            return 2
            
    ## Check If Interesting Within 2 Miles ##
    # Check If Number+1 Is Intersting
    if (nlen1 > 2):
        # Check For All Zeros After First Number
        if (snum1[1:].count('0') == len(snum1[1:])):
            return 1
        
        # Check For All Numbers The Same
        if (snum1.count(snum1[0]) == len(snum1)):
            return 1
            
        # Check For Incrementing Number
        if (snum1 in inc_str):
            return 1
            
        # Checkk For Decrementing Number
        if (snum1 in dec_str):
            return 1
        
        # Check For Palindrome
        if (is_palindrome(number1) == True):
            return 1
            
        # Check Awesome_Phrases Array
        if (number1 in awesome_phrases):
            return 1
    
    # Check If Number+2 Is Interesting
    if (nlen2 > 2):
        # Check For All Zeros After First Number
        if (snum2[1:].count('0') == len(snum2[1:])):
            return 1
        
        # Check For All Numbers The Same
        if (snum2.count(snum2[0]) == len(snum2)):
            return 1
            
        # Check For Incrementing Number
        if (snum2 in inc_str):
            return 1
            
        # Checkk For Decrementing Number
        if (snum2 in dec_str):
            return 1
        
        # Check For Palindrome
        if (is_palindrome(number2) == True):
            return 1
            
        # Check Awesome_Phrases Array
        if (number2 in awesome_phrases):
            return 1
            
    return 0
