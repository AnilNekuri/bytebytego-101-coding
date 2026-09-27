from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # Write your code here
    dummy_head = ListNode()
    dummy_head.next = head
    trailer = dummy_head
    leader = head

    #Move leader k distance from trailer
    for _ in range(k):
        if leader is None:
            return dummy_head.next
        leader = leader.next

    #Move both at the sametime
    while leader is not None:
        trailer = trailer.next
        leader = leader.next
    
    #Remove kth node from the end
    trailer.next = trailer.next.next 
    return dummy_head.next

def remove_kth_last_node_first_attempt(head: ListNode, k: int) -> ListNode:
    # Write your code here
    dummy_head = ListNode()
    dummy_head.next = head
    trailer = dummy_head
    leader = head
    index = 0
    #Move leader k distance from trailer
    while index < k:
        if leader is None:
            return dummy_head.next
        leader = leader.next
        index += 1

    #Move both at the sametime
    while leader is not None:
        trailer = trailer.next
        leader = leader.next
    
    #Remove kth node from the end
    trailer.next = trailer.next.next 
    return dummy_head.next

if __name__ == "__main__":
    # Test cases
    test_case = [1,2,4,7,3]
    k = 2

    dummy_head = ListNode(0)
    current = dummy_head
    for value in test_case:
        current.next = ListNode(value)
        current = current.next
    head = dummy_head.next

    # Reverse the linked list
    result_head = remove_kth_last_node(head=head, k=k)

    # Print the reversed linked list
    current = result_head
    result_list = []
    while current is not None:
        result_list.append(current.val)
        current = current.next
    print(result_list)    