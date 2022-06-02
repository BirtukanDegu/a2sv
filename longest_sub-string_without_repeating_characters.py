class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub = ''
    
        for l in s:
            if l in sub:
                sub = sub[sub.find(l)+1:]        
            sub += l
            if len(sub) > max_len:
                max_len = len(sub)
            
        return max_len

