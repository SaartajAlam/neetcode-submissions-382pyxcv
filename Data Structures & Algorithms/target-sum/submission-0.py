from functools import cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i, curSum):
            if i == len(nums):
                return 1 if curSum == target else 0
            return dp(i+1, curSum + nums[i]) + dp(i+1, curSum - nums[i])
        return dp(0, 0)