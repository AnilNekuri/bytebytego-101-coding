from typing import List

def maximums_of_sliding_window(nums: List[int], k: int) -> List[int]:
    # Write your code here
    result = []
    dequeue = []
    if k > len(nums):
        return result
    for i in range(k):
        while dequeue and dequeue[-1][0] <= nums[i]:
             dequeue.pop()
        dequeue.append((nums[i],i))
    result.append(dequeue[0][0])
    for i in range(k,len(nums)):
        while dequeue and dequeue[-1][0] <= nums[i]:
             dequeue.pop()
        dequeue.append((nums[i],i))
        l = i - k
        if dequeue[0][1] <= l:
            dequeue.pop(0)
        result.append(dequeue[0][0])
    return result

if __name__ == "__main__":
    # result = maximums_of_sliding_window(nums=list([3,2,4,1,2,1,1]),k=4)
    
    result = maximums_of_sliding_window(nums=list([1,3,-1,-3,5,3,6,7]),k=10)
    print('result', result)