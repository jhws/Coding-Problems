class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = max(nums)
        temp = 0
        for i in nums:
            
            temp += i
            if temp >= 0:
                s = max(s, temp)
            else:
                temp =0
            
                
        return s
        