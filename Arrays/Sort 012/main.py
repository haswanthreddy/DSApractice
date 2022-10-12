# input: {1, 0, 2, 1, 2}
# output: {0, 1, 1, 2, 2}
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

inputArr = [1,0,2,0,1,2,0,1,0,1]

def sort012(arr):
    high = len(arr) -1
    mid = 0
    low = 0
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

print(sort012(inputArr))
