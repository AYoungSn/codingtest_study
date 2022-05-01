def solve(loc, place, dist, visit):
    
    if dist > 2:
        return 1
    if dist > 0 and place[loc[0]][loc[1]] == 'P':
        print('1:',loc[0], loc[1], dist)
        return 0
    visit[loc[0]][loc[1]] = 1
    if dist == 2:
        return 1
    if dist > 0 and place[loc[0]][loc[1]] == 'X':
        return 1
    
    dxdy = [(1,0), (-1, 0), (0,1), (0,-1)]
    print(loc, dist)

    for i in range(len(dxdy)):
        x = loc[0] + dxdy[i][0]
        y = loc[1] + dxdy[i][1]
        # print('2:', y, x, dist + 1)
        if x >= 5 or y >= 5 or x < 0 or y < 0 or visit[x][y] == 1:
            continue
        print('2:', y, x, dist + 1)
        if solve((x, y), place, dist + 1, visit) == 0:
            return 0
    return 1

def solution(places):
    answer = []

    for pla in places:
        check = 1
        print(pla)
        for i in range(5):
            for j in range(5):
                if pla[i][j] == 'P':
                    print('loc: ', i, j)
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