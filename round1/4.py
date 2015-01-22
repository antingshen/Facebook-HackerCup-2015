import sys
from itertools import *
from heapq import *
from operator import mul
import math
from collections import Counter

def dot(vector1, vector2):
    return sum(map(mul, vector1, vector2))

LEAF = (1, 1, 2) # Best NUM, best COST, second COST

def solve(f):
    N = int(f.readline().strip())
    limit = int(math.sqrt(N)) + 5
    employees = {}
    managers = list(map(int, f.readline().split()))

    for i, manager in enumerate(managers):
        employee = i + 1
        if manager in employees:
            employees[manager].append(employee)
        else:
            employees[manager] = [employee]
    managers = [None] + managers

    stack = [1]
    table = [None if i in employees else LEAF for i in range(N+1)]
    while stack:
        curr = stack[-1]
        poppable = True
        for employee in employees[curr]:
            if table[employee] is None:
                stack.append(employee)
                poppable = False
        if not poppable:
            continue

        penalties = Counter()

        ideal_cost = 0
        for employee in employees[curr]:
            best_num, best_cost, second_cost = table[employee]
            ideal_cost += best_cost
            penalties[best_num] += second_cost - best_cost
            table[employee] = None

        best_num = None
        best_cost = sys.maxsize
        second_cost = None
        index = 1
        while True:
            penalty = penalties[index]
            cost = penalty + index
            if cost <= best_cost:
                second_cost = best_cost
                best_cost = cost
                best_num = index
            if penalty == 0 and second_cost is not None:
                break
            index += 1

        table[curr] = (best_num, best_cost + ideal_cost, second_cost + ideal_cost)
        stack.pop()
    return table[1][1]


def main():
    f = open("4.in", 'r')
    num_iterations = int(f.readline())

    for iteration_number in range(num_iterations):
        print(iteration_number, file=sys.stderr)
        print("Case #%d: %s" % (
            iteration_number + 1, 
            solve(f)))

main()
