class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = {}
        freq = [[] for i in range(n + 1)]

        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num,count in counts.items():
            freq[count].append(num)

        res = []
        
        for i in range(n, -1, -1):
            for f in freq[i]:
                if len(res) == k:
                    break
                res.append(f)
        return res