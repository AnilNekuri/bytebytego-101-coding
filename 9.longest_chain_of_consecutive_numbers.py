from typing import List

def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    memory = set(nums)
    longest_chain = 0

    for n in nums:
        chain = 1
        while n-1 in memory:
            chain += 1
            n-=1
        longest_chain = max(chain,longest_chain)
    return longest_chain

if __name__ == "__main__":
    test_cases = [
        [100, 4, 200, 1, 3, 2],
        [0,3,7,2,5,8,4,6,0,1],
        [1,2,0,1],
        [9,1,-3,2,4,8,3,-1,6,-2,-4,7],
        [],
        [1],
        [1,2],
        [2,1]
    ]
    for nums in test_cases:
        print(f"Input: {nums}")
        print(f"Output: {longest_chain_of_consecutive_numbers(nums)}")