from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    # Write your code here
    left = 0
    right = max(heights)
    while left < right:
        mid = (( left + right ) // 2 ) + 1
        wood_len = calc_wood_len(heights=heights,h=mid) 
        if wood_len < k:
            right = mid - 1
        else:
            left = mid
    return left    
# 0 1 2 3 4 5 6 7 8

def calc_wood_len(heights: List[int],h: int) -> int:
    wood_len = 0
    for height in heights:
        if height - h > 0:
            wood_len += height - h
    return wood_len

if __name__ == "__main__":
    heights = list([2,6,3,8])
    k = 7
    result = cutting_wood(heights=heights, k=k)
    print('result', result)