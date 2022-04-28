class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        S_nums=[];
        count=0
        for value in nums:
            for another_value in nums:
                if(value>another_value):
                    count+=1
            S_nums.append(count)
            count=0
        return S_nums
                

