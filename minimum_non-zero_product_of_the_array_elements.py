class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        modulo = 10**9+7                                
        b = 2**(p-1)-1
        a = 2**p - 2   
    
        return ((pow(a,b,modulo))*(a+1))%modulo


