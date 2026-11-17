from typing import List
from collections import Counter
import heapq 

class Pair:
    def __init__(self, str: str, freq: int):
        self.str = str
        self.freq = freq

    def __lt__(self,other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq

def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # Write your code here
    min_heap = []
    freqs = Counter(strs)
    for str, freq in freqs.items():
        heapq.heappush(min_heap,Pair(str,freq=freq))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    res = [heapq.heappop(min_heap).str for _ in range(k)]
    res.reverse()
    return res

if __name__ == "__main__":
    result = k_most_frequent_strings(strs=list(["byte","byte","go","city"]), k=2)
    print('result',result)    

