
def staircase(n):
    s = " "
    for i in range(1,n+1):
        print((s*(n-i))+("#"*i))

if __name__ == '__main__':
    n = int(input())
    staircase(n)