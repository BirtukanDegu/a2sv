class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_arr =[]
        intervals.sort()
        new_arr.append(intervals[0])
        for i in range (len(intervals)):
            if new_arr[-1][-1] >= intervals[i][0]:
                    if new_arr[-1][-1] <= intervals[i][1]:
                         new_arr[-1][-1] = intervals[i][1]
                    else:
                        continue
            else:  
                new_arr.append(intervals[i])
        return new_arr   
                    
