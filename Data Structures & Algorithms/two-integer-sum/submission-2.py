class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mappings:
                return [mappings[complement], i]
            mappings[nums[i]] = i
                