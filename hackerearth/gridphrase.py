
def vertical_mat(l,p):
    vertical = []
    count = 0
    s = 'saba'
    for i in l:
        j = list(i)
        vertical.append(j[p])
    vertical = ''.join(vertical)
    count += vertical.count(s)
    return count

def ext_dat(l,m,n,r):
    count = 0
    s = 'saba'
    
    if m == 0:
        for i in l:
            count += i.count(s)
    else:
        count += l[3].count(s)
    
    if n == 0:
        for p in range(r):
            count += vertical_mat(l,p)
    else:
        p = 3
        count += vertical_mat(l,p)
    
    diagonal_one = []
    k = 0
    for i in l:
        j = list(i)
        diagonal_one.append(j[k])
        k += 1
    diagonal_one = ''.join(diagonal_one)
    count += diagonal_one.count(s)

    diagonal_two = []
    k = len(l)-1
    for i in l:
        j = list(i)
        diagonal_two.append(j[k])
        k -= 1
    diagonal_two = ''.join(reversed(diagonal_two))
    count += diagonal_two.count(s)

    return count


def cell_matrix(l,lower,upper,lowertwo,uppertwo):
    new_mat = []
    for i in l[lowertwo:uppertwo]:
        k = list(i)
        k = k[lower:upper]
        k = ''.join(k)
        new_mat.append(k)
    return new_mat



if __name__=='__main__':
    n,m = map(int, input().rstrip().split())
    l = []
    count = 0
    for i in range(n):
        l.append(input())
    length1 = len(l[0])
    length2 = len(l)
    uppertwo = 4
    r = 4
    for i in range(n-4+1):
        upper = 4
        for j in range(m-4+1):
            new_mat = cell_matrix(l,j,upper,i,uppertwo)
            count += ext_dat(new_mat,i,j,r)
            upper += 1
        uppertwo += 1
    print(count)