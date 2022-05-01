def solve(loc, place, dist, visit):
    if dist > 2: # dist 가 2 초과인 경우는 체크할 필요 없음
        return 1
    if dist > 0 and place[loc[0]][loc[1]] == 'P':
        # dist 가 2 이하인데 사람이 있는 경우 -> 거리두기를 지키지 않음
        return 0
    visit[loc[0]][loc[1]] = 1
    if dist == 2:
        # dist 가 2인데 사람이 없었으므로 거리두기를 지킴 (더이상 갈 필요 없음)
        return 1
    if dist > 0 and place[loc[0]][loc[1]] == 'X':
        # dist 가 2 이하인데 현재 X 인 경우 파티션에 막혀있는 경로이므로 체크하지 않아도 됨
        return 1
    
    dxdy = [(1,0), (-1, 0), (0,1), (0,-1)]

    for i in range(len(dxdy)):
        x = loc[0] + dxdy[i][0]
        y = loc[1] + dxdy[i][1]
        # x, y 가 제대로된 index 인지, (x, y) 위치를 방문 안했는지 체크
        if x >= 5 or y >= 5 or x < 0 or y < 0 or visit[x][y] == 1:
            # x, y 위치에 이미 방문했으면 재방문 X
            continue
        # (x, y) 위치에 방문
        # 현재 위치에서 (x, y) 로 이동하면 dist + 1
        if solve((x, y), place, dist + 1, visit) == 0:
            return 0
    return 1

def solution(places):
    answer = []

    for pla in places:
        check = 1
        # 대기실 한 방씩 체크
        for i in range(5):
            for j in range(5):
                # [i][j] 가 P (사람이 있으면)
                if pla[i][j] == 'P':
                    # 사람을 기준으로 주변 거리를 체크 (다른 사람과의 거리)
                    visit = [[0 for _ in range(5)] for _ in range(5)]
                    if not solve((i, j), pla, 0, visit):
                        check = 0
                        break
            if not check:
                break
        answer.append(check)
    
    return answer

print(solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))