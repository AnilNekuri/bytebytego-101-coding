class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, x: int) -> None:
        self.enqueue_stack.append(x)

    def dequeue(self) -> int:
        if self.dequeue_stack:
            return self.dequeue_stack.pop()
        elif self.enqueue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack.pop()

        return None

    def peek(self) -> int:
        if self.dequeue_stack:
            return self.dequeue_stack[-1]
        elif self.enqueue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
            return self.dequeue_stack[-1]
        return None

#["enqueue(1)","enqueue(2)","dequeue()","enqueue(3)","peek()"]
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print('dequeue:',queue.dequeue())
    queue.enqueue(3)
    queue.peek()
    print('peek:',queue.peek())