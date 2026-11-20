class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        current_val = None
        for i in range(len(nums)):
            if nums[i] != current_val:
                current_val = nums[i]
                nums[k] = current_val
                k += 1
        
        return k




s = Solution()
print(s.removeDuplicates([1, 1, 2]))