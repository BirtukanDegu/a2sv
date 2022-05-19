class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        res_stack = []
        res = ''
        num = ''
        
        for i in s:
            if i.isdigit():
                num += i
            elif i.isalpha():
                res += i
            elif i == "[":
                num_stack.append(int(num))
                res_stack.append(res)
                num = ''
                res = ''
            else:
                new_str = res_stack.pop()
                repeat = num_stack.pop()
                res = new_str + res * repeat
        return res
