"""
Function Name: find_missing_letter
Description:
    Take a char array with consecutive letters
    and determine what letter was not present in
    the array.
    Ex: ["a", "b", "d", "e"] -> "c"
Input(s):
    chars - Char array
Return(s):
    Missing Char
"""
def find_missing_letter(chars):
    i = 0
    for letter in chars:
        if ((ord(letter)+1) != ord(chars[i+1])):
            return chr(ord(letter)+1)
        i += 1
    return
