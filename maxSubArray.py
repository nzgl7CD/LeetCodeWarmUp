class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return
        current_profit=nums[0]
        max_profit=nums[0]
        for i in nums[1:]:
            current_profit=max(i, current_profit+i)
            max_profit=max(max_profit, current_profit)
        return max_profit
        
        
        
        
            
        
        
        
        
    
print(Solution().maxSubArray(nums=[1,2,3,-10,2,6]))
        