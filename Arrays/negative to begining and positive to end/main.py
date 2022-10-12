'''
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/
'''

input_arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6, 0, 2]


'''

def sort_arr(arr):
    negative_index = 0
    positive_index = len(arr) -1
    while negative_index <= positive_index:
        if arr[positive_index] < 0:
            arr[positive_index], arr[negative_index] = arr[negative_index], arr[positive_index]
            negative_index += 1
        else:
            positive_index -= 1
    return arr

print(sort_arr(input_arr))

'''
        
def sortArr2(arr):
    left = 0
    right = len(arr) - 1

    while (left < right):
        if (arr[left] < 0):
            left += 1
        if (arr[right] > 0):
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
    return arr

print(sortArr2(input_arr))