
def neighbours(grid, r, c):
    vals = sum((row[c -(c>0): c+2] for row in grid[r -(r>0):r+2]), [])
    vals.remove(grid[r][c])     # rm itself.
    return vals       


grid = [[1, 0, 0, 0], 
        [0, 0, 0, 1], 
        [0, 1, 1, 0], 
        [0, 1, 0, 1]]
print(sum(neighbours(grid,2,2)))
