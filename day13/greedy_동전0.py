N, K = list(map(int, input().split()))
arr = [int(input()) for _ in range(N)]

arr.sort(reverse=True)
result = 0
count = 0
for i in range(N):
    if result + arr[i] <= K:
        cnt = (K - result) // arr[i]
        result += cnt * arr[i]
        count += cnt

print(count)