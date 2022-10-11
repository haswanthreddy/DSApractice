# python simple solution for reversing

inputArr = ['h','t','m','l','5']

'''
 simple solution
 print(inputArr[::-1])
'''


def reverse_string(arr, start, end):
    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return

reverse_string(inputArr, 0, len(inputArr)-1)

print(inputArr)