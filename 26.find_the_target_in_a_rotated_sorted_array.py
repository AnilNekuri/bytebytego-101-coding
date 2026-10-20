from typing import List

def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    # Write your code here
    left = 0
    right = len(nums) - 1
    if len(nums) == 0:
        return -1
    while left < right:
        mid = ( left + right ) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1 
    return left if nums[left] == target else -1
# 8, 9, 10, 11, 12, 1, 2, 3, 4, 5, 6, 7
if __name__ == "__main__":
    nums = list([8,1,2,3,4,5,6,7])
    target = 7
    result = find_the_target_in_a_rotated_sorted_array(nums=nums, target=target)
    print('result',result)