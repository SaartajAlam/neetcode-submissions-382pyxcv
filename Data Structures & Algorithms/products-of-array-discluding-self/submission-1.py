'''
[1,2,4,6]
prefix: [1, 2, 8, 48]
postfix: [48,48,24,6]

res = [48,24,12,8]
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        prefix[0] = nums[0]
        suffix = [0] * n
        suffix[n-1] = nums[n-1]

        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
        
        for i in range(n):
            pref = prefix[i-1] if i - 1 >= 0 else 1
            suff = suffix[i+1] if i + 1 <= n - 1 else 1
            res[i] = pref * suff
        return res
