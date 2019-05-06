




n = int(input())
arr = list(map(int, input().split()))
hscore = 0
lscore = 0
min = arr[0]
max = arr[0]
for i in arr:
    if i<min:
        lscore += 1
        min = i
    elif i>max:
        hscore +=1
        max = i
score = []
score.append(hscore)
score.append(lscore)
print(*score)
