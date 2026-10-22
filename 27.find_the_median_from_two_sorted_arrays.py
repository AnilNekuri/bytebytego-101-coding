from typing import List

def find_the_median_from_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    len_num1 = len(nums1)
    len_num2 = len(nums2)
    num3 = list([])
    mid_index = (( len_num1 + len_num2 )) // 2
    pointer1 = 0
    pointer2 = 0
    while len(num3) <= mid_index:

        if pointer1 >= len_num1 and pointer2 < len_num2:
            num3.append(nums2[pointer2])
            pointer2 += 1
            continue
        if pointer2 >= len_num2 and pointer1 < len_num1:
            num3.append(nums1[pointer1])
            pointer1 += 1
            continue

        if nums1[pointer1] < nums2[pointer2]:
            num3.append(nums1[pointer1])
            pointer1 += 1
        else:
            num3.append(nums2[pointer2])
            pointer2 += 1
            
    if (len_num1 + len_num2) % 2 == 0:
        return (num3[len(num3)-1]+num3[len(num3)-2])/2
    else:
        return num3[len(num3)-1] 

if __name__ == "__main__":
    nums1 = list([0,2,5,6,8])
    nums2 = list([1,3,7])
    result = find_the_median_from_two_sorted_arrays(nums1=nums1,nums2=nums2)
    print('result',result)
# 0 1 2 3 4 5 6 7 8 9 , len 10, Ans = (4+5)/2
# 0 1 2 3 4 5 6 7 8 , len 9, Ans = (4)
# 1 , len 1 Ans = 1
# nums1 = 0 1 2 3 4 5 6 , nums2 = 7 8 9 
# num1 = 0, num2 = 1,   
#  
