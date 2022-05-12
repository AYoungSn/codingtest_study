# 가장 긴 증가하는 부분수열
n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        if arr[j] < arr[i] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))