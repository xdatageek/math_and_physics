import re


f = open('input.txt', 'r')
next(f)
A = [int(s) for s in re.split(' +', f.readline())]
for k in range(int(f.readline())):
    c = f.readline().split()
    c1 = int(c[0])
    c2 = int(c[1])
    print(sum(A[c1:c2+1]))
