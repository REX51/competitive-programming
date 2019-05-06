import sys

def stress(arr):
    k = arr[4]
    cu = int(k/arr[0])
    t = int(cu**(1/3))
    if t < k:
        print(0)
    while(t>-1):
        if ((arr[0]*(t**3))+(arr[1]*(t**2))+(arr[2]*t)+arr[3])<=k or k==0:
            print(t)
            break
        t -= 1



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().rstrip().split()))
        stress(arr)