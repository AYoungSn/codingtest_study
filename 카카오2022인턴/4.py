from copy import deepcopy
from math import inf

nodes = None
gate = None
summit_arr = None

# fail

def solve(cur, summit, time, visit):
    if cur == summit:
        return summit, time

    min_time = inf
    for i in range(1, len(nodes)):
        if visit[i][cur] == 0 and i != cur and nodes[cur][i] != inf and i not in gate:
            if i != summit and i in summit_arr:
                break
            print('solve', i, cur)
            visit[cur][i] = 1
            visit[i][cur] = 1
            s, t = solve(i, summit, max(time, nodes[cur][i]), deepcopy(visit))
            if t < min_time:
                min_time = t
    print(summit, min_time)
    return summit, min_time

def solution(n, paths, gates, summits):
    global nodes, gate, summit_arr
    gate = gates
    summit_arr = summits
    answer = []
    # nodes = [[inf for _ in range(n + 1)] for _ in range(n + 1)]
    nodes = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visit = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i, j, w in paths:
        nodes[i][j] = w
        nodes[j][i] = w
    for k in range(1, n + 1):
        if k in summits:
            continue
        for i in range(1, n + 1):
            
            for j in range(1, n + 1):
                if i in gates and j in gates:
                    continue
                if i != j:
                    nodes[i][j] = max(nodes[i][j], max(nodes[i][k], nodes[k][j]))
                    nodes[j][i] = nodes[i][j]
    print(nodes)
    answer = [n + 1, inf]
    for g in gates:
        for s in summits:
            if answer[1] > nodes[g][s]:
                answer[0] = s
                answer[1] = nodes[g][s]
    return answer
    print(nodes)

    min_s = n + 1
    min_t = inf
    for i in range(len(gates)):
        for j in range(len(summits)):
            s, t = solve(gates[i], summits[j], 0, visit)
            if min_t > t and t != 0:
                min_t = t
                min_s = summits[j]
                
            # elif t != 0 and min_t == t and min_s > s:
            #     print(s, t)
            #     min_s = s
            #     min_t = t

    
    return (min_s, min_t)

#gates : 출입구
# summits: 산봉우리

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], 
[1], [2,3,4]))