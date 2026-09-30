from ds import ListNode
from typing import Tuple
"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def palindromic_linked_list(head: ListNode) -> bool:
    if head is None:
        return True
    tail1, head2 = split_linked_list(head)
    head2 = reverse_linked_list(head2)
    tail1.next = None
    pointer1 = head
    pointer2 = head2
    while pointer1 and pointer2:
        if pointer1.val != pointer2.val:
            return False
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return True
# Return tail, head2
def split_linked_list(head: ListNode) -> Tuple[ListNode, ListNode]:
    dummy_head = ListNode()
    dummy_head.next = head
    pointer1 = dummy_head
    pointer2 = dummy_head
    tail1 = None
    head2 = None 
    while pointer2 is not None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
        tail1 = pointer1
        head2 = tail1
        if pointer2:
            pointer2 = pointer2.next
            head2 = tail1.next
    return tail1, head2

def reverse_linked_list(head: ListNode):
    prev = None
    pointer = head
    while pointer:
        node = pointer.next
        pointer.next = prev
        prev = pointer
        pointer = node
    return prev
