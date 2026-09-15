from typing import List
import sys

def triplet_sum(nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()
    # loop nums
    target_max_index = len(nums) - 2

    for i in range(target_max_index):
        # set target to i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        # sort remaining array
        sub_nums = sorted(nums[i + 1:])
        sub_result = pair_sum(sub_nums, target)

        for result in sub_result:
            output.append([nums[i]] + result)
    return output


def pair_sum(nums: List[int], target: int) -> List[List[int]]:
    result = []
    left = 0
    right = len(nums) - 1
    while left < right:
        if left > 0 and nums[left] == nums[left - 1]:
            left += 1
            continue
        if right < len(nums) - 1 and nums[right] == nums[right + 1]:
            right -= 1
            continue

        sub_sum = nums[left] + nums[right]
        if sub_sum == target:
            result.append([nums[left], nums[right]])
            left += 1
        elif sub_sum < target:
            left += 1
        elif sub_sum > target:
            right -= 1

    return result



def main() -> int:
    if len(sys.argv) > 1:
        try:
            nums = [int(value) for value in sys.argv[1:]]
        except ValueError:
            print("Usage: python triplet_sum.py 12 3 1 2 -6 5 -8 6")
            return 1
    else:
        nums = [-1,0,1,-1,-4]

    print(triplet_sum(nums))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

