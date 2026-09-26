from ds import ListNode

"""
Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
def linked_list_reversal_recursive_first_try(head: ListNode) -> ListNode:
    if head is None:
        return head
    def reverse(node: ListNode) -> ListNode:
        if node.next is None:
            return node
        else:
            nextNode: ListNode = node.next
            tail = reverse(node=nextNode)
            nextNode.next = node
            node.next = None
            return tail
    return reverse(head)

def linked_list_reversal_recursive(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    tail = linked_list_reversal_recursive(head=head.next)
    head.next.next = head
    head.next = None
    return tail
        

def linked_list_reversal(head: ListNode) -> ListNode:
    # Write your code here 
    if head is None:
        return head
    prev_node = None
    curr_node = head
    next_node = head.next
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5],
        [1],
        [],
        [1, 2],
        [1, 2, 3]
    ]

    for case in test_cases:
        # Create linked list from the test case
        dummy_head = ListNode(0)
        current = dummy_head
        for value in case:
            current.next = ListNode(value)
            current = current.next
        head = dummy_head.next

        # Reverse the linked list
        reversed_head = linked_list_reversal_recursive(head)

        # Print the reversed linked list
        current = reversed_head
        reversed_list = []
        while current is not None:
            reversed_list.append(current.val)
            current = current.next
        print(reversed_list)