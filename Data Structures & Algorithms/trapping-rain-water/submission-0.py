class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        maxLeft, maxRight = height[l], height[r]
        while l < r:
            if maxLeft < maxRight:
                res += maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                res += maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
        return res