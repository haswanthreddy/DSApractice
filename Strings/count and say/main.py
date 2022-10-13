# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        val = "1"
        for i in range(n-1):
            char = val[0]
            count = 1
            temp_string = ""
            for j in range(1,len(val)):
                if char != val[j]:
                    temp_string = temp_string + str(count) + char
                    count = 0
                    char = val[j]
                
                count += 1
            temp_string = temp_string + str(count) + char
            val = temp_string
        return val
        