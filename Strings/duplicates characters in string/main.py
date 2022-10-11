# find duplicate characters in a string
# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
'''
input: "geeksforgeeks"
output:
count['e'] = 4
count['g'] = 2
count['k'] = 2

'''

stringInput = input().lower()

def findDuplicates1(string):
    duplicates = [0]*len(string)
    for i in string:
        if i in duplicates:
            duplicates[i] += 1
            continue
        duplicates[i] =1
    return duplicates

count = findDuplicates1(stringInput)

for key, value in count.items():
    print("count[{}]={}".format(key, value))
