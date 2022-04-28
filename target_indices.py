class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new_nums=[]
        nums.sort()
        for i in range(len(nums)):
            if(nums[i]==target):
                new_nums.append(i)
        return new_nums
