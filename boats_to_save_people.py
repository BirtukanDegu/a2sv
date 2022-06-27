class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        a,b,count=0,len(people)-1,0
        while a<=b:
            if people[a]+people[b]<=limit:
                a+=1
            b-=1
            count+=1
        if a== b:
            return count+1
        return count
        
        
