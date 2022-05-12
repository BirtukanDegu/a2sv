class Solution:
    def isValid(self, s: str) -> bool:
        flag="true"
        lst=[]
        my_dic={'[':']' , '{':'}' , '(':')'}
        for par in s:
            if par in my_dic:
                lst.append(par)
            elif len(lst)>0 and my_dic[lst[-1]]==par:
                lst.pop()
            else:
                flag=False
                break
        if len(lst)==0:
            return flag
        else:
            return False
    
            
                    
                
        
