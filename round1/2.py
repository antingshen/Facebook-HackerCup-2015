import sys
from itertools import *

OFFSET = 97

def solve(f):
    trie = [None]*26
    total = 0
    T = int(f.readline())
    for _ in range(T):
        node = trie
        word = f.readline().strip()
        for i, char in enumerate(word):
            # print(char)
            total += 1
            spot = node[ord(char)-OFFSET]
            if type(spot) == list:
                # print("list")
                node = spot
                continue
            if spot is None:
                # print("break")
                node[ord(char)-OFFSET] = word
                break
            # print("else")
            next_node = [None]*26
            node[ord(char)-OFFSET] = next_node
            if len(spot) > i + 1:
                next_node[ord(spot[i+1])-OFFSET] = spot
            node = next_node
        print(total)
    return total

def main():
    f = open("autocomplete2.txt", 'r')
    num_iterations = int(f.readline())

    for iteration_number in range(num_iterations):
        print("Case #%d: %s" % (iteration_number + 1, solve(f)))

main()
