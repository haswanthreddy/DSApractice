'''
Input: str1 = “onetwofour”, str2 = “hellofourtwooneworld” 
Output: YES 
Explanation: str1 is substring in shuffled form of str2 as 
str2 = “hello” + “fourtwoone” + “world” 
str2 = “hello” + str1 + “world”, where str1 = “fourtwoone” (shuffled form) 
Hence, str1 is a substring of str2 in shuffled form.

Input: str1 = “roseyellow”, str2 = “yellow” 
Output: NO 
Explanation: As the length of str1 is greater than str2. Hence, str1 is not a substring of str2.
'''


def subStringCheck(str1: str, str2: str) -> bool:
    if len(str1) > len(str2):
        return False
    result = {}
    for i in str2


print(subStringCheck(input(), input()))