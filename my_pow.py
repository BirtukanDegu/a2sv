class Solution:
    def myPow(self, x: float, n: int) -> float:
        # return x**n
        if n < 0:
            x = 1 / x
            n = -n
        answer = 1
        while n:
            if n%2:
                answer *= x
            x *= x
            n //= 2
        return answer
        
