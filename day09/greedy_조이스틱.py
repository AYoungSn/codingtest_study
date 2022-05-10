# 시작 위치는 항상 맨 앞

def solution(name):
    answer = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cur = 0
    min_move = len(name) - 1
    while cur < len(name):
        idx = alpha.index(name[cur])
        answer += min(idx, 25 - idx + 1)
        next = cur + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([
                min_move, 
                2 * cur + len(name) - next, # A 앞의 원소들을 돌고 뒤로 넘어갈 것인지
                cur + 2 * (len(name) - next)]) # A 뒤의 원소들을 먼저 돌고 앞으로 넘어올 것인지
        cur += 1
    return min_move + answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))