# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))
        dummy = cur = ListNode()
        while heap:
            val, index, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
            cur.next = node
            cur = cur.next
        return dummy.next