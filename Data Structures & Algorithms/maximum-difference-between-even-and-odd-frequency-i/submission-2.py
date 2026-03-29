class Solution:
    def maxDifference(self, s: str) -> int:
        map = {}
        oddCount, evenCount = 0, float("inf")

        for ch in s:
            map[ch] = 1 + map.get(ch, 0)
        for v in map.values():
            if v % 2 == 0:
                evenCount = min(evenCount, v)
            else:
                oddCount = max(oddCount, v)

        return oddCount - evenCount
