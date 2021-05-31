
# convert list to string
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "
    str1 = str1.rstrip()
    # return string
    return str1