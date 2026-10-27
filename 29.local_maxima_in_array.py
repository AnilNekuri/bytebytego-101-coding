from typing import List

def local_maxima_in_array(nums: List[int]) -> int:
    # Write your code here
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid
         
    return left

if __name__ == "__main__":
    #nums: List[int] = list([1,4,3,2,3])
    #nums: List[int] = list([1,2,3,4,5])
    nums: List[int] = list([5,4,3,2,1])
    result = local_maxima_in_array(nums=nums)
    print('result', result)    
