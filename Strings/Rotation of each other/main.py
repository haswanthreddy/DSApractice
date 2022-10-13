# input: s1 = ABCD, s2 = CDAB | check if there are reversed or not
# output: strings are rotation of each other
# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/


'''
string1 = "ACBDCABC"
string2 = "CDABBCCA"

def checkIfRotated(string1,string2) -> bool:
    if len(string1) != len(string2):
        return 'strings are not rotation of each other'

    # string 
    i = 0
    while (i < len(string1)):
        s1 = ''
        s2 = ''
        if i == 0:
            s1 = string1[i:i+2]
            s2= string2[2-len(string1)-i:]
        else:
            s1 = string1[i:i+2]
            s2= string2[(-len(string1)-i):-i]
     
        if s1 != s2:
            return False
        i += 2
    return True
    
print(checkIfRotated(string1,string2))

'''

# alternate solution





    