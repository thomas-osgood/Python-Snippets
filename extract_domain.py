"""
Function that, when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""
def domain_name(url):
    retVal = "" 
    
    if (url[:4] == "http"):
        url = url.split("//")[1].split('.')
        if (url[0] == "www"):
            retVal = url[1]
        else:
            retVal = url[0]
    elif (url[:3] == "www"):
        retVal = url.split('.')[1]
    else:
        retVal = url.split('.')[0]
    
    return retVal
