class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        total_max=nums[0]
        current_total=nums[0]
        
        for i in nums[1:]:
            current_total=max(i, i+current_total)
            total_max=max(total_max,current_total)
        return total_max
        
        
        
            
        
        
        
        
    
print(Solution().maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
        