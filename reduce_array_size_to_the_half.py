class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        new_dic = Counter(arr)
        values = sorted(new_dic.values())
        counter = 0
        final = 0
        while final < len(arr)/2:
            final += values.pop()
            counter +=1
        return counter

