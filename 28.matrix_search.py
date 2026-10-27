from typing import List
from typing import Tuple

def matrix_search(matrix: List[List[int]], target: int) -> bool:
    len_rows: int = len(matrix)
    if len_rows == 0:
        return False
    len_cols: int = len(matrix[0])
    if len_cols == 0:
        return False 
    left: int = 0
    right: int = len(matrix) * len(matrix[0]) - 1
    while left <= right:
        mid = (left + right) // 2
        r, c = find_row_col(mid, len_rows=len_rows, len_cols=len_cols)

        if target == matrix[r][c]:
            return True
        elif target > matrix[r][c]:
            left = mid + 1
        else: 
            right = mid - 1
    # r, c = find_row_col(flat_index=left, len_rows=len_rows,len_cols=len_cols)
    # if target == matrix[r][c]:
    #     return True
    return False

def find_row_col(flat_index: int, len_rows: int, len_cols: int) -> Tuple[int, int]:
    row_index = flat_index // len_cols
    col_index = flat_index % len_cols
    return row_index, col_index

if __name__== "__main__":
    matrix: List[List[int]] = [[1]]
    target: int = 1
    result: bool = matrix_search(matrix=matrix, target=target)
    print('result', result)