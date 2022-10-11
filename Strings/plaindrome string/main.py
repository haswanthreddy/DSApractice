# check if given string is palindrome
# https://practice.geeksforgeeks.org/problems/palindrome-string0817/1


stringInput = input("enter string: ")

def check_palindrome (string) -> bool:
    start = 0
    end = len(string) -1
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

print('Given string is palidrome' if check_palindrome(stringInput) else 'Given string is palidrome')




# simple method time complexity O(n) space complexity O(1)
'''

print('Given string is palidrome' if stringInput[::-1] == stringInput else 'Given string is not palidrome')

print('Given string is palidrome' if ''.join(reversed(stringInput)) == stringInput else 'Given string is not palidrome')

'''

# recursion time complexity O(n) , space complexity O(n)

def palindromeCheck2 (string) -> bool:
    length = len(string)
    if length < 2:
        return True
    elif string[0] == string[length-1]:
        return palindromeCheck2(string[1 : length-1])
        
    return False

print('Given string is palidrome' if palindromeCheck2(stringInput) else 'Given string is not a palindrome')
