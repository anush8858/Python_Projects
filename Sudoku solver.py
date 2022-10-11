def row_valid(row, col, grid, k):
    for i in range(9):
        if grid[row][i] == k:
            return False
    return True
def column_valid(row, col, grid, k):
    for i in range(9):
        if grid[i][col] == k:
            return False
    return True
    
    def subbox_valid(row, col, grid, k):
    for i in range(0, 9, 3):
        if row >= i and row  < i+3:
            row_start = i
            row_end = i+3
        
        if col >= i and col < i+3:
            col_start = i
            col_end = i+3 
    
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if grid[i][j] == k:
                return False
                    return True

def valid(row, col, grid, k):
    if (row_valid(row, col, grid, k) and column_valid(row, col, grid, k) and subbox_valid(row, col, grid, k)):
        return True
    
    return False
def SUDOKU(i, j, grid):
    ## Base case 
    if i == len(grid):
        return True
    if grid[i][j] != 0:
        if j == 8:
            #chang the row(new row)
            return SUDOKU(i+1, 0, grid)
        else:
            #chang the col
            return SUDOKU(i, j+1, grid)
                for k in range(1, 10):
        if valid(i, j, grid, k):
            grid[i][j] = k
            if j==8:
                if(SUDOKU(i+1, 0, grid)):
                    return True
            else:
                if(SUDOKU(i, j+1, grid)):
                    return True
                      grid[i][j] = 0
    
    return False
    
def main(grid):
    #If sol find then True, else False
    print(SUDOKU(0, 0, grid))


global grid
grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] 
        ]

main(grid)
print(*row)
