from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # Write your code here
    row_memory = [set() for _ in range(9)]
    column_memory = [set() for _ in range(9)]
    grid_memory = [[set() for _ in range(3)] for _ in range(3)]
    rows = len(board)
    cols = len(board[0])
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == 0:
                continue
            elif (board[row][col] in row_memory[row] or 
                board[row][col] in column_memory[col] or 
                board[row][col] in grid_memory[row//3][col//3]):
                return False
            else:
                row_memory[row].add(board[row][col])
                column_memory[col].add(board[row][col])
                grid_memory[row//3][col//3].add(board[row][col])
    return True

if __name__ == "__main__":
    test_cases = [[[3,0,6,0,5,8,4,0,0],
                   [5,2,0,0,0,0,0,0,0],
                   [0,8,7,0,0,0,0,3,1],
                   [1,0,2,5,0,0,3,2,0],
                   [9,0,0,8,6,3,0,0,5],
                   [0,5,0,0,9,0,6,0,0],
                   [0,1,0,0,0,0,0,7,4],
                   [0,3,0,0,0,8,2,5,0],
                   [0,0,5,2,0,6,0,0,0]]]
    
    for test in test_cases:
        print('verify_sudoku_board',test,'result',verify_sudoku_board(test))