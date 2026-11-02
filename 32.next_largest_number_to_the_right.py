from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    # Write your code here
    
    if len(nums) == 0:
        return list([])
    len
    result = [0] * len(nums)
    stack = []
    for i in range(len(nums)-1, -1, -1):
        if len(stack) == 0:
            result[i] = -1
            stack.append(nums[i])
        else:
            while len(stack) >0 and stack[-1] <= nums[i]:
                stack.pop()
            if len(stack) >0:
                result[i] = stack[-1]
                stack.append(nums[i])
            else:
                result[i] = -1
                stack.append(nums[i])
    return result

if __name__ == "__main__":
    result = next_largest_number_to_the_right(list([5,2,4,6,1]))
    print('resut', result)