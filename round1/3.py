import sys
from itertools import *
def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

MOD = 1000000007
sys.setrecursionlimit(40000)

@memodict
def stressfree(scores):
    my_score, op_score = scores
    if my_score < 0 or op_score < 0:
        return 0
    if my_score <= op_score:
        return 0
    if my_score + op_score == 1:
        return 1
    return (stressfree((my_score - 1, op_score)) + stressfree((my_score, op_score - 1))) % MOD

@memodict
def stressful(scores):
    my_score, op_score = scores
    if my_score < 0 or op_score < 0:
        return 0
    if my_score > op_score:
        return 0
    if my_score + op_score == 0:
        return 1
    return (stressful((my_score - 1, op_score)) + stressful((my_score, op_score - 1))) % MOD

def main():
    sys.setrecursionlimit(40000)
    f = open("3.in", 'r')
    num_iterations = int(f.readline())

    for iteration_number in range(num_iterations):
        my_final, op_final = map(int, f.readline().strip().split('-'))
        print("Case #%d: %s %s" % (
            iteration_number + 1, 
            stressfree((my_final, op_final)),
            stressful((op_final, op_final))))

main()
