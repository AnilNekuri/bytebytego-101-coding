class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class DoublyLinkedListNode:
   def __init__(self, key: int, val: int):
       self.key = key
       self.val = val
       self.next = self.prev = None