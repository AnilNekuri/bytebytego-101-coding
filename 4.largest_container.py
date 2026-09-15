from typing import List

def largest_container(heights: List[int]) -> int:
    # Write your code here
    largest_container = 0
    left = 0
    right = len(heights)-1
    while(left < right):
        container = min(heights[left],heights[right])*(right-left)
        largest_container = max(largest_container,container)
        if(heights[left] < heights[right]):
            left+=1
        elif(heights[left] > heights[right]):
            right-=1
        else:
            left+=1
            right-=1
        
    return largest_container
def main():
    test_cases = [
        [1,5,4,2],
        [2,7,8,3,7,6]
    ]
    for test in test_cases:
        result = largest_container(heights=test)
        print('largest_container',result)

if __name__ == "__main__":
    main()