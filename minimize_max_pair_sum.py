class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr=[]
        i=0
        for k in range(len(nums)//2):
            arr.append(nums[i] + nums[len(nums) - 1 - i]) 
            i+=1
        
        return max(arr)
            
        
