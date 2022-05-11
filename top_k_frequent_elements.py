class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = collections.Counter(nums)
        return heapq.nlargest(k, arr, key=arr.get)
