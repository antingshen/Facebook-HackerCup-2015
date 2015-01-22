import sys
from itertools import *
import copy
import pprint

pp = pprint.PrettyPrinter(indent=2)

def solve(f):
	num_rows, num_cols = map(int, f.readline().split())
	grid = []
	turrets = []
	for row_num in range(num_rows):
		row = []
		line = f.readline()
		for col_num in range(num_cols):
			char = line[col_num]
			if char in "<^>v":
				turrets.append([row_num, col_num, char])
			if char == "S":
				start = (row_num, col_num)
				row.append(".")
				continue
			if char == "G":
				end = (row_num, col_num)
				row.append(".")
				continue
			row.append(char)
		grid.append(row)
	grids = [copy.deepcopy(grid) for _ in range(4)]
	
	for turret in turrets:
		for grid in grids:
			shoot_turret(turret, grid)
			turret[2] = rotate_turret[turret[2]]

	fringe = [(0, start[0], start[1], 0)]
	while fringe:
		grid_ind, row, col, time = fringe.pop(0)
		grid_ind = next_grid[grid_ind]
		grid = grids[grid_ind]
		time += 1
		for row_offset, col_offset in offsets:
			new_row = row + row_offset
			new_col = col + col_offset
			if new_row < 0 or new_row >= num_rows:
				continue
			if new_col < 0 or new_col >= num_cols:
				continue
			char = grid[new_row][new_col]
			if char == ".":
				if (new_row, new_col) == end:
					return time
				grid[new_row][new_col] = time
				fringe.append((grid_ind, new_row, new_col, time))
			else:
				assert type(char) == int or char in "#<v^>+"

	return "impossible"

rotate_turret = {
			"<" : "^",
			"^" : ">",
			">" : "v",
			"v" : "<"}

offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))

next_grid = {
	0:1, 1:2, 2:3, 3:0
}

def shoot_turret(turret, grid):
	try:
		row, col, char = turret
		grid[row][col] = char
		increment = 1 if char in ">v" else -1
		while True:
			if char in "<>":
				col += increment
				if col < 0:
					return
			else:
				row += increment
				if row < 0:
					return
			current = grid[row][col]
			if current in "<v^>#":
				return
			if current in "S.G":
				grid[row][col] = "+"
				continue
			assert current == "+", current
	except IndexError:
		return


def main():
	f = open("laser_maze.txt", 'r')
	num_iterations = int(f.readline())

	for iteration_number in range(num_iterations):
		print("Case #%d: %s" % (iteration_number + 1, solve(f)))

main()

