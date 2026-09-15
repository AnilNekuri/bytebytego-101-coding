from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    # Write your code here
    left = 0
    right = 0
    size = len(nums)
    while right < size:
        if nums[right] == 0:
            right+=1
            continue
        if nums[right] != 0:
            #swap nums[left] and nums[right]
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left+=1
            right+=1 

def main():
    test_cases = [
        [0,1,0,3,12],
        [0,0,1],
        [1,2,3],
        [0,0,0],
        [4,5,0,6,0,7]
    ]
    for test in test_cases:
        shift_zeros_to_the_end(nums=test)
        print('shift_zeros_to_the_end',test)
if __name__ == "__main__":
    main()