class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == k: return 1
            else: return 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        count = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i] == k:
                    count += 1
        return count
            
        
