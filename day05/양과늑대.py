from collections import defaultdict
from copy import deepcopy
import itertools

num_edge = defaultdict(list)
w_info = list() # wolf 위치
max_sheep = 0

def solve(cur, visit, wolf, sheep, can_go):
    global max_sheep
    if visit[cur]: return # 이미 방문한 노드는 체크하지 않음
    visit[cur] = True

    if w_info[cur] == 1: # 현재 위치에 늑대가 있으면
        wolf += 1 # 늑대 수 증가
    else:
        sheep += 1 # 양의 수 증가
        max_sheep = max(max_sheep, sheep) # 모을 수 있는 양의 최대 수 계산
    
    if wolf >= sheep: # 늑대가 더 많거나 같으면 더이상 계산하지 않음
        return
    can_go.extend(num_edge[cur]) # 방문 예정 리스트에 자식들을 추가
    for node in can_go:
        # 방문할 예정인 리스트에서 node 를 방문할 것이므로 방문예정 목록에서는 제외
        go = [loc for loc in can_go if loc != node and not visit[loc]]
        solve(node, deepcopy(visit), wolf, sheep, go)
    

def solution(info, edges):
    global num_edge, w_info
    w_info = info
    # 부모 노드의 번호로 자식 노드를 찾을 수 있도록 dict 만들기
    for e in edges:
        num_edge[e[0]].append(e[1]) # { 부모: [자식1, 자식2], ,,}
    visit = [False] * len(info) # 방문한 곳인지 체크하는 리스트
    solve(0, visit, 0, 0, [])
    return max_sheep


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], 
[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

def solution2(info, edges): # 순열을 사용한 경우 - 시간초과
    answer = 1
    edge_dict = {}
    for i in range(len(edges)):
        # edge_dict[edges[i][0]].append(edges[i][1])
        edge_dict[edges[i][1]] = edges[i][0] # { 자식: 부모, 자식1:부모1.,,}
    edge_dict[0] = 0
    for case in itertools.permutations(range(1, len(info)), len(info) - 1):
        if edge_dict[case[0]] != 0:
            continue
        visit = [False for _ in range(len(info))]
        visit[0] = True
        valid = True
        wolf = 0
        sheep = 1
        for i in range(len(case)):
            if visit[edge_dict[case[i]]] == False:
                valid = False
                break
            else:
                visit[case[i]] = True
                if info[case[i]] == 0:
                    sheep += 1
                else:
                    wolf += 1
                if sheep <= wolf:
                    sheep = 0
                    break
                if answer < sheep:
                    answer = sheep
        if not valid:
            continue
    return answer