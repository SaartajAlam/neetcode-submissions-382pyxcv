class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        k = len(nums) - 1
        l, r = 0, len(nums)-1
        while l <= r:
            leftSquared = nums[l] * nums[l]
            rightSquared = nums[r] * nums[r]
            if leftSquared < rightSquared:
                res[k] = rightSquared
                r -= 1
            else:
                res[k] = leftSquared
                l += 1
            k -= 1
        return res