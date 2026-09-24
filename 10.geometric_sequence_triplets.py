from typing import List

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    left_map = {}
    right_map = {}
    triplets = 0
    for n in nums:
        right_map[n] = right_map.get(n,0) + 1
    for x in nums:
        right_map[x] = right_map[x]-1
        if x%r == 0:
            triplets += (left_map.get(x//r,0) * right_map.get(x*r,0)) 
        left_map[x] = left_map.get(x,0) + 1
    return triplets

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 4], 2),
        ([1, 3, 9, 9, 27, 81], 3),
        ([1, 5, 5, 25, 125], 5),
        ([1, 2, 3, 4], 2),
        ([1, 1, 1], 1),
        ([1, 2, 4], 2),
        ([1, 3, 9], 3),
        ([1, 5, 25], 5)
    ]
    for nums,r in test_cases:
        print(f"Input: {nums}, r={r}")
        print(f"Output: {geometric_sequence_triplets(nums,r)}")