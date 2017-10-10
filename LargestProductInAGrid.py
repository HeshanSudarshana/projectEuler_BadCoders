grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)
greatest = 0
for i in range(20):
    for j in range(20):
        if j<=16:
            p = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
            if p>greatest:greatest=p
        if i<=16:
            p = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
            if p>greatest:greatest=p
        if i<=16 and j<=16:
            p = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
            if p>greatest:greatest=p
        if i<=16 and j<=16:
            p = grid[19-i][j]*grid[18-i][j+1]*grid[17-i][j+2]*grid[16-i][j+3]
            if p>greatest:greatest=p
print(greatest)