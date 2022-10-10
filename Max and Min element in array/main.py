# max and min element in an array
# https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
# input: arr[] = {3,5,4,1,9}
# output: min: 1, max: 9


inputArr = [3,5,4,1,9]

# inbuilt python methods
'''
print('max', max(inputArr))
print('min', min(inputArr))

'''


# using hashtable


result = { "max": inputArr[0], "min": inputArr[0] }

for i in inputArr:
    if (result["max"] < i):
        result["max"] = i
    
    if (result["min"] > i):
        result["min"] = i
        
print(result)


# using other ways check geeks for geek


