from itertools import *
R=range
for C in R(input()):N=raw_input();A=[int("".join(P))for P in permutations(N)if sum(P[i]!=N[i]for i in R(len(N)))==2and P[0]!="0"]+[int(N)];print "Case #%s: %s %s"%(C+1,min(A),max(A))