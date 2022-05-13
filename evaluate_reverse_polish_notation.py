class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=[]
        result = 0
        for value in tokens:
            if value == '+':
                a=arr.pop()
                b=arr.pop()
                result = b + a
                arr.append(result)
                # continue
            elif value=='-':
                a=arr.pop()
                b=arr.pop()
                result = b - a
                arr.append(result)
                # continue
            elif value=='*':
                a=arr.pop()
                b=arr.pop()
                result = b * a
                arr.append(result)
                # continue
            elif value =='/':
                a=arr.pop()
                b=arr.pop()
                result = (b / a)
                # print(b,a,result)
                arr.append(int(result))
                # continue
            else:
                arr.append(int(value))
       
        return arr.pop()
