def solution(name):
    answer = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cur = 0
    min_move = len(name) - 1

    while cur < len(name):
        idx = alpha.index(name[cur])
        if idx <= 13:
            answer += idx
        else:
            answer += 25 - idx + 1

        next = cur + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        min_move = min(min_move, cur + len(name) - next)
        cur += 1

    return min_move + answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZ"))