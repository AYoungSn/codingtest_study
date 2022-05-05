from copy import deepcopy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
block = None

#방문한곳 체크, 현재 플레이어의 좌표, 상대 플레이어의 좌표
def solve(visit, aloc, bloc):
    if visit[aloc[0]][aloc[1]]:
        return 0
    cur = aloc
    ret = 0

    visit[cur[0]][cur[1]] = 1
    for i in range(4):
        x = cur[0] + dx[i] # row
        y = cur[1] + dy[i] # col
        # print(y, x)
        if x < 0 or x >= len(visit) or 0 > y or y >= len(visit[0])\
            or visit[x][y] == 1 or block[x][y] == 0:
            continue
        val = solve(visit, bloc, (x, y)) + 1
        
        # ret == 현재 저장된 이동 횟수
        # val == 새로 계산된 이동 횟수
        # 이동 횟수가 짝수면 패배, 홀수면 승리
        if ret % 2 == 0 and val % 2 == 1:
            # 새로 계산된 턴이 승리인 경우 갱신
            ret = val
        elif ret % 2 == 0 and val % 2 == 0:
            # 이전과 새로 계산된 턴 모두 패배인 경우 최대값
            ret = max(val, ret) # 최대한 더 많이 이동하는 걸로 선택
        elif ret % 2 == 1 and val % 2 == 1:
            # 이전과 이후 모두 승리이 경우
            ret = min(ret, val) # 최대한 조금만 이동하여 이기는 걸로 선택
    visit[cur[0]][cur[1]] = 0
    return ret


def solution(board, aloc, bloc):
    global block
    if len(board) == 1 and len(board[0]) == 1:
        return 0
    if aloc == bloc:
        return 1
    block = board    
    return solve([[0] * len(board[0]) for _ in range(len(board))], aloc, bloc)


print(solution([[1]], [0,0], [0,0]))
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))