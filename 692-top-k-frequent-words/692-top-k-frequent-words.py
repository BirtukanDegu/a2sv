class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d=dict()
        for i in words:
            if i not in d:
                d[i]=words.count(i)
        d=sorted(d.items(), key=lambda x:(-x[1],x[0]))
        ans=[]
        i=0
        while k:
            ans.append(d[i][0])
            i+=1
            k-=1
        return ans