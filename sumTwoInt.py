class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b!=0:
            carry= a & b
            a=a^b
            b=carry<<1
        stack=[1 for i in range(a)]
        return sum(stack)
        
            
        
a,b=2,3
print(Solution().getSum(a,b))