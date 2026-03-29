class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                index, value = stack.pop()
                res[index] = i - index
            stack.append([i, v])
        return res