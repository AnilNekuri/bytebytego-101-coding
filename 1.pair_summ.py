from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    left = 0
    right = len(nums) - 1
    
    while left < right:
        psum = nums[left] + nums[right]
        print('left ',left, nums[left],'right',nums[right],psum)
        if psum > target:
            right = right - 1
        elif psum < target:
            left = left + 1
        elif psum == target:
            return [left, right]
        
    
    return []