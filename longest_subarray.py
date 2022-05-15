class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        beg = 0
        l = 0
        mp = {}
        for end in range(len(nums)):
            if nums[end] in mp:
                mp[nums[end]] += 1
            else:
                mp[nums[end]] = 1
            mini = min(mp)
            maxi = max(mp)
            if maxi - mini <= limit:
                if l < end - start + 1:
                    l = end - start + 1
                    beg = start
            else:
                while start < end:
                    mp[nums[start]] -= 1
                    if mp[nums[start]] == 0:
                        mp.pop(nums[start])
                    start += 1
                    mini = min(mp)
                    maxi = max(mp)
                    if maxi - mini <= limit:
                        break
        return l
