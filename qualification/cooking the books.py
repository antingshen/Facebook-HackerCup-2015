import sys
from itertools import *

def solve(in_string):
	in_string = in_string.strip()
	digit_list = list(in_string)
	smallest = int(in_string)
	largest = int(in_string)
	for first_ind, second_ind in combinations(range(len(digit_list)), 2):
		first = digit_list[first_ind]
		second = digit_list[second_ind]
		if second == '0' and first_ind == 0:
			continue
		if first == second:
			continue
		copy = list(digit_list)
		copy[second_ind] = first
		copy[first_ind] = second
		result = int("".join(copy))
		smallest = min(smallest, result)
		largest = max(largest, result)
	return "%d %d" % (smallest, largest)


def main():
	f = open("cooking_the_books.txt", 'r')
	num_iterations = int(f.readline())

	for iteration_number in range(num_iterations):
		print("Case #%d: %s" % (iteration_number + 1, solve(f.readline())))

main()

