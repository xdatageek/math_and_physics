f = open('input.txt', 'r')
next(f)
A = [int(i) for i in f.readline().split()]
for k in range(int(f.readline())):
    c = f.readline().split()
    c1 = int(c[1])
    c2 = int(c[2])
    if c[0] == '1':
        S = 0
        for j in range(c1, c2+1):
            S += A[j]
        print(S)
    else:
        A[c1] = c2
