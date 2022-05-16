n = int(input())
arr = list(map(int, input().split()))

def solve(n, arr):
    arr.sort()
    for i in range(1, n):
        arr[i] += arr[i - 1]
    return sum(arr)

print(solve(n, arr))