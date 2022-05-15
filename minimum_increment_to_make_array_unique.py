class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if nums == [] or len(nums)==1: 
            return 0
        nums.sort()                    
        s, ans, mx = set(), 0, nums[0] 
        for num in nums:
            if num in s:               
                mx = mx + 1            
                ans += (mx - num)      
                s.add(mx)              
            else:
                s.add(num)
                mx = max(mx, num)
        return ans

