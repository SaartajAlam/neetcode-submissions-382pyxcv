class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        maxOdd = float("-inf")
        minEven = float("inf")
        for v in counter.values():
            if v % 2:
                maxOdd = max(maxOdd, v)
            else:
                minEven = min(minEven, v)
        return maxOdd - minEven