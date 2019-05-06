
def plusminus(arr):
    pos = 0
    neg = 0
    nil = 0
    for _ in arr:
        if _ > 0:
            pos += 1
        elif _ < 0:
            neg += 1
        else:
            nil += 1
    pos_ratio = pos/len(arr)
    neg_ratio = neg/len(arr)
    nil_ratio = nil/len(arr)
    print(pos_ratio)
    print(neg_ratio)
    print(nil_ratio)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusminus(arr)

