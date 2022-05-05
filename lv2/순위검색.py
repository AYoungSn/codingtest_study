from collections import defaultdict
import itertools


def solution(info, query): # 정확성 테스트 통과
    answer = [0 for _ in range(len(query))]
    i = 0
    for que in query:
        q = [i for i in que.split(' ') if i != 'and']
        for per in info:
            p = per.split()
            if ((q[0] == '-' or p[0] == q[0]) and \
                (q[1] == '-' or p[1] == q[1]) and (q[2] == '-' or p[2] == q[2]) \
                and (q[3] == '-' or p[3] == q[3]) and int(p[4]) >= int(q[4])):
                print(p[2], q[2])
                answer[i] += 1

        i += 1
                
    return answer

def solution2(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        temp = i.split()
        key = temp[:-1]
        score = int(temp[-1])

        for i in range(5):
            # 현재 리스트들로 나올 수 있는 모든 가지수의 조합을 계산
            # 1 개: [1, 2, 3] -> [[1], [2], [3]]
            # 2 개: [1, 2, 3] -> [[1, 2], [1, 3], [2, 3]]
            # 3 개: [1, 2, 3] -> [[1,2,3]]
            combi = itertools.combinations(key, i)
            for c in combi:
                # 조합 리스트를 문자열로 바꿔서 딕셔너리의 키로 저장
                info_dict[''.join(c)].append(score)

    # print(info_dict)

    for k in info_dict.keys():
        info_dict[k].sort()

    for qu in query:
        qu = [q for q in qu.split() if q != 'and' and q != '-']
        # print(qu)
        query_score = int(qu[-1])
        query_key = ''.join(qu[:-1])
        if query_key in info_dict:
            scoreList = info_dict[query_key]
            # print('info_dict[', query_key, ']', info_dict[query_key])
            left, right = 0, len(scoreList)
            # 이진 탐색
            while left < right:
                mid = (left + right)//2
                if scoreList[mid] >= query_score:
                    right = mid
                else:
                    left = mid + 1
            answer.append(len(scoreList) - right) 
        else:
            answer.append(0)

    return answer

print(solution2(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))