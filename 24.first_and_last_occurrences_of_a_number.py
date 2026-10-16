from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> List[int]:
    result = [-1,-1]
    if len(nums) == 0 or target > nums[len(nums)-1] or target < nums[0]:
        return list(result)

    result = [-1,-1]
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = ( left + right ) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            right = mid
    if nums[left] == target:
        result[0] = left

    left = 0
    right = len(nums) - 1
    while left < right:
        mid = ((left + right) // 2 ) + 1
        if nums[mid] > target:
            right = right - 1
        elif nums[mid] < target:
            left = left + 1
        else:
            left = mid
    if nums[right] == target:
            result[1] = right
    return list(result)

if __name__ == "__main__":
    nums = list([1,3,4,5,6,7,8,9,10,10,10])
    target = 10
    result = first_and_last_occurrences_of_a_number(nums=nums, target=target)
    print('result',result)