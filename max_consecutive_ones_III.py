class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count, result, i = 0, 0, 0
        for j in range(len(nums)):
            if nums[j] == 0:
                count += 1
            while count > k:
                if nums[i] == 0:
                    count -= 1
                i = i+1
            result = max(result, j-i+1)
        return result
