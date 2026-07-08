class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = {}
        for i, num in enumerate(nums):
            if target - num in nums_index:
               return [nums_index[target - num], i]
            nums_index[num] = i
        return []


s = Solution()
print(s.twoSum([2,7,11,15], 9))