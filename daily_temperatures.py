class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]
        for i, t1 in enumerate(temperatures):
            while stack and t1 > stack[-1][1]:
                j, t2 = stack.pop()
                res[j] = i - j
            stack.append((i, t1))
        return res
