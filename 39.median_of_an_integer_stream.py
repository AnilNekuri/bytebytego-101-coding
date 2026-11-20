import heapq

class MedianOfAnIntegerStream:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.total_heap_size = 0

    def add(self, num: int) -> None:
        if len(self.maxheap) == 0:
            heapq.heappush(self.maxheap, -num)
        else:
            if -self.maxheap[0] >= num:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        self.total_heap_size = len(self.maxheap) + len(self.minheap)
        max_size_maxheap = 0 
        if self.total_heap_size % 2 == 0:
            max_size_maxheap = self.total_heap_size//2
        else:
            max_size_maxheap = (self.total_heap_size+1)//2
        if len(self.maxheap) > max_size_maxheap:
            while len(self.maxheap) > max_size_maxheap:
                max_num_from_maxheap = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap,max_num_from_maxheap)
        else:
            while len(self.maxheap) < max_size_maxheap:
                min_num_from_minheap = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap,-min_num_from_minheap)


    def get_median(self) -> float:
        if self.total_heap_size == 0:
            return
        elif self.total_heap_size % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0])/2
        else:
            return -self.maxheap[0]


if __name__ == "__main__":
    median_stream = MedianOfAnIntegerStream()

    median_stream.add(3)
    median_stream.add(6)
    print(median_stream.get_median())
    median_stream.add(1)
    print(median_stream.get_median())
