from typing import List

def zero_striping(matrix: List[List[int]]) -> None:
    if len(matrix) == 0:
            return
    pass

def zero_striping_approach1(matrix: List[List[int]]) -> None:
    if len(matrix) == 0:
        return
    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)

    for r in range(rows):
        for c in range(cols):
            if (r in zero_rows or
                c in zero_cols):
                matrix[r][c] = 0

if __name__ == "__main__":
    test_cases = [
        [[1,2,3],
         [4,0,6],
         [7,8,9]],
        [[1,2,3],
         [4,5,6],
         [7,8,9]],
        [[0,2,3],
         [4,5,6],
         [7,8,9]],
        [[1,2,3],
         [4,5,6],
         [7,8,0]]
    ]
    for test in test_cases:
        zero_striping(test)
        print('zero_striping',test)