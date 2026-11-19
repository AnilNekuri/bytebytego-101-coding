from typing import List
from ds import ListNode
import heapq 

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    # Write your code here
    result: ListNode = ListNode(-1)
    ListNode.__lt__ = lambda self, other: self.val < other.val
    heap = []
    for head in lists:
        if head:
            heapq.heappush(heap, head)    
    curr = result
    while heap:
        smallNode: ListNode = heapq.heappop(heap)
        curr.next = smallNode
        curr = curr.next

        if smallNode.next:
            heapq.heappush(heap, smallNode.next)
    return result.next

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    return values


if __name__ == "__main__":
    data = [[1, 6], [1, 4, 6], [3, 7]]

    linked_lists = [build_linked_list(values) for values in data]
    result = combine_sorted_linked_lists(linked_lists)

    print(linked_list_to_list(result))