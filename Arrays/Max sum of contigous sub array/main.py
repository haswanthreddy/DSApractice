#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_sum = arr[0]
        temp_max_sum = arr[0]
        decreased = False
        for i in range(1,len(arr)):
            if decreased:
                print("decreased", max_sum, temp_max_sum, arr[i])
                if  (temp_max_sum + arr[i]) > max_sum: 
                    max_sum = temp_max_sum + arr[i]
                    decreased = False
                else:
                    temp_max_sum += arr[i]
            else:
                print("continue", max_sum, temp_max_sum, arr[i])
                if (max_sum + arr[i]) >= max_sum:
                    max_sum += arr[i]
                else :
                    temp_max_sum = max_sum + arr[i]
                    decreased = True
                    
            if arr[i] > max_sum:
                print("inside last if")
                max_sum = arr[i]
                decreased = False
        return max_sum if max_sum >= temp_max_sum else temp_max_sum
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends



# solution 2 working solution

def maxSubArraySum2(self,arr,N):
        ##Your code here
        max_sum = float('-inf')
        sum = 0
        for i in arr:
            sum = sum + i
            if sum > max_sum:
                max_sum = sum
            if sum < 1 :
                sum = 0
        return max_sum



