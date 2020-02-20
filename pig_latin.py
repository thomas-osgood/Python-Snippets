"""
Function Name: pig_it
Description:
    Function takes a string as an input and
    returns the Pig Latin version of the string.
Input(s):
    text - String to convert
Return(s):
    new_snt - Converted text
"""
def pig_it(text):
    wrd_lst = text.split()
    new_snt = ""
    new_wrd = ""
    
    for word in wrd_lst:
        if word.isalpha():
            new_wrd = word[1:] + word[0] + "ay"
            new_snt += new_wrd + " "
        else:
            new_snt += word + " "
    
    new_snt = new_snt[:-1]
    return new_snt
    
if __name__ == "__main__":
    pig_it("Make this pig latin")
