# approach 

#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    # currIndex , len , jump
	    curr_index = 0
	    jump = arr[0]
	    total_jumps = 0
	    max_jump = 0
	    max_jump_index = 0
	    for i in range(1,n):
	        if curr_index + jump >= n-1:
	            return total_jumps + 1
	        if max_jump <= arr[i] and arr[i] != 0:
	           max_jump = arr[i]
	           max_jump_index = i
	       
	        if curr_index + jump == i:
	            curr_index = max_jump_index
	            max_jump_index = 0
	            jump = max_jump
	            max_jump = 0
	            total_jumps += 1
	   
	    return -1 if total_jumps == 0 else total_jumps + 1
	            
	            
	  

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends


# working solution

#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    if (n <= 1):
	        return 0
	    if (arr[0] == 0):
	        return -1
        
        max_reach = arr[0]
        steps = arr[0]
        jumps = 1
        for i in range(1,n):
            steps -= 1
            if i == n -1:
                return jumps
            max_reach = max([arr[i] + i, max_reach])
            
            if steps == 0:
                if i >= max_reach:
                    return -1
                jumps += 1
                steps = max_reach - i
        return jumps        
	            
	            
	  

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends
