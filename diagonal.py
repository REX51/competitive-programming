import os

def diagonal(arr):
    sum1 = 0
    sum2 = 0
    j = 0
    l = len(arr)-1
    for i in arr:
        sum1 += i[j]
        sum2 += i[l]
        j += 1
        l -= 1
    if sum1>sum2:
        return sum1-sum2
    else:
        return sum2-sum1

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    result = diagonal(arr)
    print(result)
