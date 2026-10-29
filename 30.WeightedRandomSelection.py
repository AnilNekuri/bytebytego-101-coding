from typing import List
import random 

class WeightedRandomSelection:
    def __init__(self, weights: List[int]):
        self.prefix_sum: List[int] = list([0])
        for i in range(1,len(weights)+1):
            self.prefix_sum.append(self.prefix_sum[i-1] + weights[i-1])
        print(self.prefix_sum)

    def select(self) -> int:
        left = 1
        right = len(self.prefix_sum)-1
        random_num = random.randint(1,self.prefix_sum[-1])
        while left < right:
            mid = ( left + right ) // 2 
            if self.prefix_sum[mid] < random_num:
                left = left + 1
            else:
                right = mid
        return (left - 1)


if __name__ == "__main__":
    weights: List[int] = list([3,1,2,4])
    randomSelection = WeightedRandomSelection(weights=weights)
    for _ in range(sum(weights)):
        result = randomSelection.select()
        print('result', result)