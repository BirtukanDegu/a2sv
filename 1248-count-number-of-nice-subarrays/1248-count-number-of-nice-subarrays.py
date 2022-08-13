class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        d = 1
        dists = []
        for n in nums:
            if n % 2 == 1:
                dists.append(d)
                d = 1
                continue
            d += 1
        dists.append(d)
        ret = 0
        for i, d1 in enumerate(dists):
            if i+k >= len(dists):
                break
            d2 = dists[i+k]
            ret += d1*d2
        return ret