class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hMap = defaultdict(int)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                hMap[stack.pop()] = num
            stack.append(num)
        
        res = [0] * len(nums1)
        count = 0
        for num in nums1:
            res[count] = hMap[num] if hMap[num] > 0 else -1
            count += 1
        return res
