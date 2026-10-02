from ds import MultiLevelListNode

def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    # Write your code here
    if not head:
        return head
    current_node:MultiLevelListNode = head
    tail: MultiLevelListNode = head
    # iterate to tail
    while tail.next:
        tail = tail.next
    while current_node:
        if current_node.child:
            tail.next = current_node.child
            while tail.next:
                tail = tail.next
            current_node.child = None
        current_node = current_node.next
    return head
