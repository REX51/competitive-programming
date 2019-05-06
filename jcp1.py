n = input()
n = int(n)
a = range(n)
b = range(n)
m = []
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]
s=0


for i in range(n):
    big1 = -1
    for i in a:
        if i > big1:
            big1 = i
    a.remove(big1)
    big2 = -1
    for i in b:
        if i > big2:
            big2 = i
    b.remove(big2)
    j = big1-big2
    print(j)
    if j < 0:
        m.append(j*(-1))
    else:
        m.append(j)
    print(a)
    print(b)

s = sum(m)

print(s%((10**9)+7))