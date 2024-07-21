class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:  
        total_produc=1  
        zeros=0
        for i in nums:
            if i == 0: 
                zeros+=1
                if zeros>1: return [0 for i in range(len(nums))]
            else: total_produc*=i
        result=[]

        for i in nums:
            if i!=0: 
                if zeros>0: result.append(0)
                else:
                    result.append(int(total_produc//i))
            else:
                result.append(total_produc)
        return result
    
nums=[-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))
        