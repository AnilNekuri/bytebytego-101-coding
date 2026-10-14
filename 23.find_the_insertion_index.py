from typing import List

def find_the_insertion_index(nums: List[int], target: int) -> int:
    # Write your code here
    left = 0
    right = len(nums)
    while left != right:
        mid = ( right + left ) // 2
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] >= target:
            right = mid
    return left

if __name__ == "__main__":
    nums = list([1,2,4,5,7,8,9])
    target = 6
    result = find_the_insertion_index(nums=nums, target=target)
    print('result',result)