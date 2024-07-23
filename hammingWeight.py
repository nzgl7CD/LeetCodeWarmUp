class Solution:
    def hammingWeight(self, n: int) -> int:
        carry=0
        while n:
            carry+=n&1
            n>>=1
        return carry

print(Solution().hammingWeight(11))