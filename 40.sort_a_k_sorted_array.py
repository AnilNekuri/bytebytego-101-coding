from typing import List
import heapq

def sort_a_k_sorted_array(nums: List[int], k: int) -> List[int]:
    # Write your code here
    min_heap = []
    min_heap = nums[:min(k+1,len(nums))]
    heapq.heapify(min_heap)
    if k < len(nums):
        for i in range(k+1, len(nums)):
            nums[i-k-1] = heapq.heappop(min_heap)
            heapq.heappush(min_heap,nums[i])
    for i in range(max(len(nums)-k-1,0),len(nums)):
        nums[i] = heapq.heappop(min_heap)
    return nums

if __name__ == "__main__":
    nums = [5,1,9,4,7,10]
    k = 2
    result = sort_a_k_sorted_array(nums=nums, k=k)
    print('result', result)