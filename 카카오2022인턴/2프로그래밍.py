target = 0

def solve(arr1, arr2, sum1, sum2, n):
    p1 = []
    p2 = []
    l, r = 0, 0
    result1 = 0
    while True:
        
        if l >= len(arr1):
            break
        if result1 > target:
            result1 -= arr1[l]
            l += 1
            continue
        if r >= len(arr1):
            break
        if result1 < target:
            result1 += arr1[r]
            r += 1
            continue
        if result1 == target:
            p1.append((l, r - 1))
            break
    
    result2 = 0
    l, r = 0, 0
    while True:
        
        if l >= len(arr2):
            break
        if result2 > target:
            result2 -= arr2[l]
            l += 1
            continue
        if r >= len(arr2):
            break
        if result2 < target:
            result2 += arr2[r]
            r += 1
            continue
        if result2 == target:
            p2.append((l, r - 1))
            break
    print(p1, p2)
    c1 = 3000000
    for l, r in p1:
        if l < n and r < n:
            c1 = min(c1, r + 1 + n + l)
        else:
            c1 = min(c1, r + 1 + l - n)

    for l, r in p2:
        if l < n and r < n:
            c1 = min(c1, r + 1 + n + l)
        else:
            c1 = min(c1, r + 1 + l - n)

    if c1 == 3000000:
        return -1
    return c1

def solution(queue1, queue2):
    global target
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2) // 2

    if (sum1 + sum2) % 2 != 0 or sum1 == sum2:
        return 0
    n = len(queue1)
    return solve(queue1 + queue2, queue2 + queue1, sum1, sum2, n)


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1,1], [1,5]))
print(solution([1,1,1,1,1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2,2,2,2]))
print(solution([1,1,1,1,1,1,1,1,1,1,1,1], [2,2,2,2,2,2,2,2,2,2,2,2]))
print(solution([222222222222222222222], [222222222222222222222]))