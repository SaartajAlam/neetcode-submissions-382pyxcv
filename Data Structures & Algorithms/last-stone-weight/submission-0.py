class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
       stones = [-s for s in stones]
       heapq.heapify(stones)
       while len(stones) >= 2:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if (x == y):
                continue
            else:
                heapq.heappush(stones, x - y)
       return 0 if not stones else -stones[0]
        

        