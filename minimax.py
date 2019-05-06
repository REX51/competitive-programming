
def minimax(arr):
    arr = sorted(arr)
    sum1 = 0 
    sum2 = 0
    for i in range(len(arr)-1):
        sum1 += arr[i]
    for i in range(1,len(arr)):
        sum2 += arr[i]
    print(sum1, sum2)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    minimax(arr)