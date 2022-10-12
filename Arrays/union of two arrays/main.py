'''
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
'''

arr1 = [1,2,3]

arr2 = [1,2,3,4,5]

def unionOfTwoSets(arr1, arr2):
    print(len(set(arr1+arr2)))

unionOfTwoSets(arr1, arr2)

