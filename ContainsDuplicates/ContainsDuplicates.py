class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) == 0:
            return False
        return len(nums) != len(set(nums))
