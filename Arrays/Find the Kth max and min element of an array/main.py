# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
# check other methods

'''
Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
Output: 10 

'''

inputArr = [7, 10, 3, 20, 15]

k = 3

inputArr = sorted(inputArr)

print(inputArr)
print('smallest:', inputArr[k-1])
print('largest:', inputArr[len(inputArr)-k])

