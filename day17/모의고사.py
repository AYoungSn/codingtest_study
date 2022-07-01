def solution(answers):
    answer = []
    per = {
        1: [1,2,3,4,5],
        2: [2,1,2,3,2,4,2,5],
        3: [3,3,1,1,2,2,4,4,5,5]
    }
    cnt = [0,0,0]
    for i in range(len(answers)):
        if per[1][i % len(per[1])] == answers[i]:
            cnt[0] += 1
        if per[2][i % len(per[2])] == answers[i]:
            cnt[1] += 1
        if per[3][i % len(per[3])] == answers[i]:
            cnt[2] += 1
    max_cnt = max(cnt)
    for i in range(len(cnt)):
        if max_cnt == cnt[i]:
            answer.append(i + 1)
    return answer

print(solution([1,2,3,4,5]))
print(solution(1,3,2,4,2))