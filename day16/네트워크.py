def dfs(visitor, computers, r, c):
    if visitor[r][c] == 1:
        return
    visitor[r][c] = 1
    visitor[c][r] = 1
    visitor[r][r] = 1
    visitor[c][c] = 1

    arr = []
    for i in range(len(computers)):
        if computers[r][i] == 1 and r != i:
            arr.append((r, i))
            # dfs(visitor, computers, r, i)
        if computers[i][c] == 1 and i != c:
            arr.append((i, c))
            # dfs(visitor, computers, i, c)
    print('v',visitor)
    print('arr', arr)
    for a in arr:
        dfs(visitor, computers, a[0], a[1])

def solution(n, computers):
    answer = 0
    visitor = [[0 for _ in range(len(computers))] for _ in range(len(computers))]
    for i in range(1, len(computers)):
        for j in range(i):
            if visitor[i][j] == 0 and computers[i][j] == 1:
                print(i, j)
                answer += 1
                dfs(visitor, computers, i, j)
    print(visitor)
    for i in range(len(visitor)):
        if visitor[i][i] == 0:
            answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))