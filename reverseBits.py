class Solution:
    def reverseBits(self, n: int) -> int:
        return int(f'{n:032b}'[::-1], 2)  
    
    def fastest_reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))

        return res  
