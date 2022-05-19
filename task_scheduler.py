class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        size = len(tasks)
        c = Counter(tasks)
        most_common, num = c.most_common(1)[0]
        max_c = 0
        
        for i in c:
            if c[i] == num:
                max_c += 1
        
        return max(size, max_c + (n+1)*(num-1))
