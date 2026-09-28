from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    pointerA, pointerB = head_A, head_B

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else head_B
        pointerB = pointerB.next if pointerB else head_A
    return pointerA 

def linked_list_intersection__first_atempt(head_A: ListNode, head_B: ListNode) -> ListNode:
    # Write your code here 
    pointer1 = head_A
    pointer2 = head_B
    p1_null_count = 0
    p2_null_count = 0

    while pointer1 is not None and pointer2 is not None:
        if pointer1 == pointer2:
            return pointer1

        if pointer1.next is None and p1_null_count == 0:
            pointer1 = head_B
            p1_null_count = 1
        else:
            pointer1 = pointer1.next

        if pointer2.next is None and p2_null_count == 0:
            pointer2 = head_A
            p2_null_count = 1
        else:
            pointer2 = pointer2.next

    return None