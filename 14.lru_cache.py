       
from ds import DoublyLinkedListNode

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoublyLinkedListNode(-1,-1)
        self.tail = DoublyLinkedListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # find in hash
        if key not in self.hashmap:
            return -1
        #print('key :',key)
        node: DoublyLinkedListNode = self.hashmap.get(key)
        # remove from DL
        node.prev.next = node.next
        node.next.prev = node.prev
        # add to the front
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        # return value
        return node.val

    def print_doubly_linked_list(self) -> None:
        node = self.head.next
        entries = []
        while node is not self.tail:
            entries.append(f"({node.key}, {node.val})")
            node = node.next
        print(" <-> ".join(entries))

    def put(self, key: int, value: int) -> None:
        # get from hash
        node = None
        if key not in self.hashmap:
            node = DoublyLinkedListNode(key=key,val=value)
            # put in to DL front

        else:
            node = self.hashmap.get(key)
            # remove if exist
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.hashmap[key] = node

        #print('b4 len : ',len(self.hashmap))
        if len(self.hashmap) > self.capacity:
            node = self.tail.prev
            node.prev.next = node.next
            node.next.prev = node.prev
            self.hashmap.pop(node.key)
        #print('aft len : ',len(self.hashmap))
        # update hash
        

if __name__ == "__main__":
        cache = LRUCache(3)
        cache.put(1, 100)
        # print('1')
        # cache.print_doubly_linked_list()
        cache.put(2, 250)
        # print('2')
        # cache.print_doubly_linked_list()
        print(cache.get(2))
        # print('3')
        # cache.print_doubly_linked_list()
        cache.put(4, 300)
        # print('4')
        # cache.print_doubly_linked_list()
        cache.put(3, 200)
        # print('5')
        # cache.print_doubly_linked_list()
        print(cache.get(4))
        # print('6')
        # cache.print_doubly_linked_list()
        print(cache.get(1))
        # print('7')
        # cache.print_doubly_linked_list()
    