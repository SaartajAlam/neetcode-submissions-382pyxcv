class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minH = [-num for num in nums]
        heapq.heapify(minH)
        for i in range(k-1):
            heapq.heappop(minH)
        return -minH[0]