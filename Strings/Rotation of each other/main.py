# input: s1 = ABCD, s2 = CDAB | check if there are reversed or not
# output: strings are rotation of each other
# https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/


string1 = "ABACD"
string2 = "CDABA"

def rotateString(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    temp_string = s*2
    count = 0
    for i in range(len(temp_string)):
        next_temp_string = temp_string[i+1] if i+1 <= (len(temp_string)-1) else ""
        next_goal = goal[count+1] if count+1 <= (len(goal)-1) else ""
        if count == (len(goal) -1):
            return True
        if temp_string[i] == goal[count] and next_temp_string == next_goal:
            count += 1
        else:
            count = 0
        
    return False

print(rotateString(string1,string2))


'''
testCases

"vcuszhlbtpmksjleuchmjffufrwpiddgyynfujnqblngzoogzg"
"fufrwpiddgyynfujnqblngzoogzgvcuszhlbtpmksjleuchmjf"

'''

    