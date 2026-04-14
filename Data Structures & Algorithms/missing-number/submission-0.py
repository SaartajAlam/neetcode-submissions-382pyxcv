class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = sum(i for i in range(len(nums) + 1))
        actual = sum(nums)

        return expected - actual