N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[0]))

print(arr)
t = 0
cnt = 0
for a in arr:
    if a[0] >= t:
        cnt += 1
        t = a[1]
        print(a)

print(cnt)