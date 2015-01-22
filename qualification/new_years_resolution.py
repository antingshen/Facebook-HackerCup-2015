import sys
from itertools import *

def solve(f):
	Gp, Gc, Gf = map(int, f.readline().split())
	num_foods = int(f.readline())
	foods = []
	for i in range(num_foods):
		foods.append(tuple(map(int, f.readline().split())))

	def can_be_done(Gp, Gc, Gf):
		if min((Gp, Gc, Gf)) < 0:
			return False
		if Gp == Gc == Gf == 0:
			return True
		for Fp, Fc, Ff in foods:
			if can_be_done(Gp-Fp, Gc-Fc, Gf-Ff):
				return True
		return False

	return "yes" if can_be_done(Gp, Gc, Gf) else "no"


def main():
	f = open("new_years_resolution.txt", 'r')
	num_iterations = int(f.readline())

	for iteration_number in range(num_iterations):
		print("Case #%d: %s" % (iteration_number + 1, solve(f)))

main()

