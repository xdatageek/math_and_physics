def cnt(nums):
    res = l = 0
    for r in range(len(nums)):
        if nums[r]:
            l = r + 1
        res = max(res, r - l + 1)
    return res
f = open('input.txt', 'r')
next(f)
A = [int(i) % 2 for i in f.readline().split()]
for k in range(int(f.readline())):
    c = f.readline().split()
    c1 = int(c[1])
    c2 = int(c[2])
    if c[0] == '1':
        print(cnt(A[c1:c2+1]))
    else:
        A[c1] = c2 % 2
