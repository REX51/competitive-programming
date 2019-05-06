

def equilateral(n,s):
    if n == s:
        s = 1
        print(s)
    elif n < 7:
        for i in range(0,n-3):
            s += 6*i+1
        print(s)
    elif n > 6:
        j = 3
        for i in range(0,j):
            s += 6*i+1
        for i in range(j,n-1,2):
            s += 6*i+4
        print(s)


if __name__ == '__main__':
    n = int(input())
    s = 3
    equilateral(n,s)