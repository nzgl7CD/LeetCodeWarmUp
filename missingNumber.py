class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        array_sum = sum(nums)
        return total_sum - array_sum

nums=[0,3,1]
print(Solution().missingNumber(nums))