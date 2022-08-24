class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = Counter(nums)
        mat = [[d[i], i] for i in d]
        mat.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(mat[i][1])
        return ans