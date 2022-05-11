class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []
        if sorted(arr) == arr:
            return answer
        else:
            target = sorted(arr)
            for i in range(len(arr)-1,-1,-1):
                pivot = arr.index(target[i])
                if pivot != i:
                    answer.append(pivot + 1)
                    arr = arr[pivot::-1] + arr[pivot +1:]
                    answer.append(i + 1)
                    arr = arr[i::-1] + arr[i+1:]
            return answer
      
        
