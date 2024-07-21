class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        validation=set()
        for i in nums:
            if i in validation: return True
            else: validation.add(i)
        return False    
    
    def better(self, nums: list[int]) -> bool:
        seen = set()
        return any(num in seen or seen.add(num) for num in nums)
                
nums=[1,2,3,2]
print(Solution().better(nums=nums))