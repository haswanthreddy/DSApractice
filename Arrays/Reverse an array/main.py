# reverse an array
# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
# input: arr [] = {1,2,3}
# output: arr [] = {3,2,1}



inputArr = [10,21,32,43,55,68,79]

#simple solution O(n)
'''
result = [0 for i in range(len(inputArr))]

for i in range(len(inputArr)):
    result[i] = inputArr[len(inputArr)-i-1]

print(result)

'''



# O(n/2) => O(n) little bit better

'''
length = len(inputArr)
for i in range(length//2):
    temp = inputArr[i]
    inputArr[i] = inputArr[length - i - 1]
    inputArr[length - i - 1] = temp

print(inputArr)

'''



# simple method using list slicing
'''
print(inputArr[::-1])

'''


# recursion
'''

def reverseList(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseList(arr, start+1,end-1)

reverseList(inputArr,0,len(inputArr)-1)
print(inputArr)

'''



# while loop and function

def reverseList(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
 

reverseList(inputArr,0, (len(inputArr)-1)) # reference being passed
print(inputArr)


