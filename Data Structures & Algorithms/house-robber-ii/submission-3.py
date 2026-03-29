class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dp(nums):
            m = len(nums)
            if m == 1:
                return nums[0]
            arr = [0] * m
            arr[0] = nums[0]
            arr[1] = max(nums[0], nums[1])
            for i in range(2, m):
                arr[i] = max(arr[i-1], arr[i-2] + nums[i])
            return arr[-1]
        
        return max(dp(nums[:-1]), dp(nums[1:]))
            