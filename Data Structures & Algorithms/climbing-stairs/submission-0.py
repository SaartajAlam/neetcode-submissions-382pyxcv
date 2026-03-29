from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            return dp(i+1) + dp(i+2)
        return dp(0)