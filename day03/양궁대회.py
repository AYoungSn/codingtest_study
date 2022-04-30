import itertools


def solution(n, info):
    answer = []
    arr = []
    max_num = 0
    win = False
    for i in range(len(info)):
        arr.append((10 - i, info[i] + 1))
    for rec in itertools.combinations_with_replacement(range(0, 11), n):
        # 모든 경우의 수(중복조합)
        now = [0 for _ in range(11)]
        lion = 0
        apeach = 0
        for r in rec:
            now[10 - r] += 1
        for n in range(len(now)): # lion 과 apeach 의 점수 배열을 순회하면서 점수 체크
            if now[n] == info[n] == 0:
                continue
            if now[n] > info[n]: # 라이언이 더 크면 라이언 점수 +
                lion += (10 - n)
            elif now[n] <= info[n]: # 어피치가 라이언보다 크거나 같으면 점수 +
                apeach += (10 - n)
        if lion > apeach:
            win = True
            if (lion - apeach) > max_num: # 점수 차이가 가장 큰 것을 골라야 한다.
                max_num = lion - apeach
                answer = now
    if not win:
        return [-1]
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))