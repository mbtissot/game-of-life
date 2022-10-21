import numpy as np

def view(grid):
	grid_final=''
	n = np.matrix(grid).shape
	for i in range(n[0]):
		row = ''
		for j in range(n[1]):
			if j == n[1]-1:
				row = row+str(grid[i][j])
			else:
				row = row + str(grid[i][j]) + ''
		row = row + '\n'
		grid_final = grid_final+row
	print(grid_final)

def update(grid):
	gridf = []
	subgrid = []
	n = np.matrix(grid).shape
	for i in range(n[0]):
		subgrid=[]
		for j in range(n[1]):
			state = (grid[i][j]=='⬜')
			spot = check(i, j, grid, state)
			subgrid.append(spot)
		gridf.append(subgrid)
	return gridf

def check(row, col, grid, state):
	mat = np.matrix(grid).shape
	endcol = mat[1]-1
	endrow = mat[0]-1
	# conds = *(col!=0 or row!=0) + *(col!=0) + *(col!=0 or row!=endrow)// *(row!=0) + *(row!=endrow)/\
	# *(row!=0 or col!=endcol) + *(col!=endcol) + *(col!=endcol or row!=endrow)
	if row==0:
		if col==0:
			neighbours = grid[row][col+1] + grid[row+1][col] + grid[row+1][col+1]
		elif col==endcol:
			neighbours = grid[row][col-1] + grid[row+1][col-1] + grid[row+1][col]
		elif (col!=endcol and col!=0):
			neighbours = grid[row][col-1] + grid[row][col+1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
	elif row==endrow:
		if col==0:
			neighbours = grid[row][col+1] + grid[row-1][col] + grid[row-1][col+1]
		elif col==endcol:
			neighbours = grid[row][col-1] + grid[row-1][col-1] + grid[row-1][col]
		else:
			neighbours = grid[row][col-1] + grid[row][col+1] + grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
	elif col==0:
		if row==0:
			neighbours = grid[row][col+1] + grid[row+1][col] + grid[row+1][col+1]
		elif row==endrow:
			neighbours = grid[row][col+1] + grid[row-1][col] + grid[row-1][col+1]
		else:
			neighbours = grid[row-1][col]+grid[row+1][col] + grid[row-1][col+1] + grid[row][col+1] + grid[row+1][col+1]
	elif col==endcol:
		if row==0:
			neighbours = grid[row][col-1] + grid[row+1][col-1] + grid[row+1][col]
		elif row==endrow:
			neighbours = grid[row][col-1] + grid[row-1][col-1] + grid[row-1][col]
		else:
			neighbours = grid[row-1][col]+grid[row+1][col]+grid[row-1][col-1]+grid[row][col-1]+grid[row+1][col-1]
	else:
		neighbours = grid[row-1][col-1] + grid[row][col-1] + grid[row+1][col-1] +\
					 grid[row-1][col] + grid[row+1][col] +\
					 grid[row-1][col+1] + grid[row][col+1] + grid[row+1][col+1]
	char = '⬜'*state*(neighbours.count('⬜')==2 or neighbours.count('⬜')==3) + '⬜'*(not state)*(neighbours.count('⬜')==3)
	if char!='⬜':
		char = '⬛'
	return char



'''	#if (row==0 or row==np.matrix(grid).shape[0]) and (col==0 or row==np.matrix(grid).shape[1]):
	if row==0:
		if col==0:
			neighbours = grid[row][col+1] + grid[row+1][col] + grid[row+1][col+1]
		elif col==np.matrix(grid).shape[1]:
			neighbours = grid[row][col-1] + grid[row-1][col] + grid[row-1][col-1]
		else:
			neighbours = grid[row][col-1] + grid[row][col+1] + grid[row+1][col-1] + grid[row+1][col] + grid[row+1][col+1]
	elif row==np.matrix(grid).shape[0]:
		if col==0:
			neighbours = grid[row][col+1] + grid[row-1][col] + grid[row-1][col+1]
		elif col==np.matrix(grid).shape[1]:
			neighbours = grid[row][col-1] + grid[row+1][col] + grid[row+1][col-1]
		else:
			neighbours = grid[row][col-1] + grid[row][col+1] + grid[row-1][col-1] + grid[row-1][col] + grid[row-1][col+1]
	elif col==0:'''



'''

grid = [['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬜','⬛','⬜','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬜','⬜','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
        ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛']]

'''