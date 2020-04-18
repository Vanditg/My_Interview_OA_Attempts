"""
Robots
"""
def dfs(grid, i1, j1, i2, j2, memo):
	m = len(grid)
    n = len(grid[0])
	if (i1 >= m or j1 < 0 or j1 >=n or i2 >= m or j2 < 0 or j2 >= n):
		return float('-inf')
	if memo[i1][j1][i2][j2] != None:
        return memo[i1][j1][i2][j2]
	if i1 == m-1 and j1 == 0 and i2 == m-1 and j2 == n-1:
		return grid[i1][j1] + grid[i2][j2]
	res = 0
	if i1 == i2 and j1 == j2:
		res += grid[i1][j1]
	else:
		res += grid[i1][j1] + grid[i2][j2]
    
	next_ =  max(max(
					max(dfs(grid, i1+1, j1, i2+1, j2, memo), max(dfs(grid, i1+1, j1, i2+1, j2-1, memo), dfs(grid, i1+1, j1, i2+1, j2+1, memo))),
					max(dfs(grid, i1+1, j1-1, i2+1, j2, memo), max(dfs(grid, i1+1, j1-1, i2+1, j2-1, memo), dfs(grid, i1+1, j1-1, i2+1, j2+1, memo)))),
					max(dfs(grid, i1+1, j1+1, i2+1, j2, memo), max(dfs(grid, i1+1, j1+1, i2+1, j2-1, memo), dfs(grid, i1+1, j1+1, i2+1, j2+1, memo))))
	res += next_
	memo[i1][j1][i2][j2] = res
	return memo[i1][j1][i2][j2]
    
def solve(grid):
	m = len(grid)
    n = len(grid[0])
    memo = [[[[None]*n for _1 in range(m)] for _2 in range(n)] for _3 in range(m)]
	return max(0, dfs(grid, 0, 0, 0, len(grid[0]) - 1, memo))
      
def main():
    dims = stdin.readline().strip().split()
    m, n = int(dims[0]), int(dims[1])
    matrix_elems = stdin.readline().strip().split()
    grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(matrix_elems.pop(0)))
        grid.append(row)
    count = solve(grid)
    print(count)
    
main()