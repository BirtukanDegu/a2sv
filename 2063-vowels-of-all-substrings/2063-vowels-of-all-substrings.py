class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        c=0
        ans=0
        for i in range(len(word)):
            if word[i] in ['a','e','i','o','u']:
                c+=1      # for all substrings from this point, vowels accumulated
                c+=i      # for all substrings till this point, the count of vowel is accumulated
            ans+=c
        return ans