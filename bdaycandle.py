

def cake(arr):
    arr = sorted(arr, reverse=True)
    count = 0
    p = arr[0]
    for i in arr:
        if p == i:
            count += 1
    print(count)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    cake(arr)