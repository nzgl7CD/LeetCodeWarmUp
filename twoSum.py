class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    num_to_index = {}
    for i, num in enumerate(nums):
      complement = target - num
      if complement in num_to_index:
        return [num_to_index[complement], i]
      num_to_index[num] = i
    return []
  
object=Solution()
print(object.twoSum([1,2,3,4,5], 7))        