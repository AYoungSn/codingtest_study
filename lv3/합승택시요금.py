from math import inf

def solution(n, s, a, b, fares):
    answer = 0
    graphs = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(len(fares)):
        graphs[fares[i][0]][fares[i][1]] = fares[i][2]
        graphs[fares[i][1]][fares[i][0]] = fares[i][2]
        answer += fares[i][2]
    
    for k in range(1, n + 1): # 경유지
        for i in range(1, n + 1): # 출발지
            for j in range(1, n + 1): # 목적지
                if i == j:
                    graphs[i][j] = 0
                if i != j:
                    graphs[i][j] = min(graphs[i][j], graphs[i][k] + graphs[k][j])
                    graphs[j][i] = graphs[i][j]
    # 모든 노드의 최소 거리 구해진 상태
    for k in range(1, n + 1):
        # s -> k -> a , k -> b 경로의 가중치 합 구하기
        answer = min(answer, graphs[s][k] + graphs[k][a] + graphs[k][b])
    # solve([0] * n, s)
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))