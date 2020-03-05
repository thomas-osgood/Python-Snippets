import re

def alphanumeric(password):
    """
    Use Regular Expression to check for only alphanumeric
    characters in a string (a-z, A-Z, 0-9). No spaces or 
    special characters allowed.
    """
    retVal = False
    pattern = re.compile("^[a-zA-Z0-9]+$".format(len(password)))
    if not(pattern.match(password) is None):
        retVal = True
    
    return retVal
