class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer=[]
        flag=True
        for i in range(len(l)):
            new_arr=nums[l[i]:r[i]+1]
            new_arr.sort()

            for j in range(len(new_arr)-1):
                if (new_arr[j+1]-new_arr[j]==new_arr[1]-new_arr[0]):
                    flag=True
                else:
                    flag=False
                    break
            answer.append(flag)
                    
        return answer
            
            
