import sys
from itertools import *

B = 10**7
s = [0] * (B + 1)
sqrtn = int(round(B**0.5))
for i in range(2, B + 1):
    if s[i] == 0:
        j = i
        while j <= B:
            s[j] += 1
            j += i

def solve(A, B, K):
    return len(list(filter(lambda x: x == K, s[A:B+1])))

def main():
    f = open("1.in", 'r')
    num_iterations = int(f.readline())

    for iteration_number in range(num_iterations):
        A, B, K = map(int, f.readline().split())
        print("Case #%d: %s" % (iteration_number + 1, solve(A, B, K)))

main()
