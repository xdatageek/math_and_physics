def cnt(x):
    return max(map(len, ''.join(map(str, x)).split('0')))
with open('input.txt', 'r') as f:
    lines = f.readlines()
A = [(int(i[-1]) + 1) % 2 for i in lines[1].split()]
out = []
for line in lines[3:]:
    c = [int(i) for i in line.split()]
    if c[0] == 1:
        out.append(cnt(A[c[1]:c[2]+1]))
    else:
        A[c[1]] = (c[2] + 1) % 2
print('\n'.join([str(k) for k in out]))
