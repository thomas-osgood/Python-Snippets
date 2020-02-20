"""
Function Name: is_valid_IP
Description:
    Function to validate whether a string is a 
    valid IP address.
Input(s):
    strng - IP address to validate
Return(s):
    True - IP address valid
    False - IP address invalid
"""
def is_valid_IP(strng):
    if (strng == ""):
        return False
    
    has_space = False
    parts = strng.split('.')
    
    if (len(parts) != 4):
        return False
    
    for part in parts:
        if (" " in part):
            has_space = True
            
        try:
            p = int(part)
        except:
            return False
        
        if ((p < 0) or (p > 255) or ((len(part) > 1) and (part[0] == "0")) or has_space):
            return False        
    
    return True
