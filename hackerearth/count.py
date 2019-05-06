
def count(a,x,l,r,n):
    new_count = []
    mat = []
    for i in range(n):
        c = 0
        mat = a[l[i]-1:r[i]]
        mat = sorted(mat)
        for j in mat:
            if x[i]%j == 0:
                c += 1
        new_count.append(c)
    print(*new_count)


if __name__ == '__main__':
    n = int(input())
    a = tuple(map(int, input().split()))
    q = int(input())
    l = tuple(map(int, input().split()))
    r = tuple(map(int, input().split()))
    x = tuple(map(int, input().split()))
    count(a,x,l,r,n)
    