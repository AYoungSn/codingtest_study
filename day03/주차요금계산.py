

from collections import defaultdict

def func(item):
    return item[1]

def solution(fees, records):
    answer = []
    record_dict = defaultdict(list)
    minute = {}
    cost = {}
    for r in records:
        rec = r.split()
        m = int(rec[0][:2]) * 60 + int(rec[0][3:]) # 00:00 시각을 기준으로 시간을 분으로 변환
        record_dict[rec[1]].append((m, rec[2])) # 차량번호: [(시간, IN/OUT), ()]
        minute[rec[1]] = 0
        cost[rec[1]] = 0
    for key, values in record_dict.items():
        if len(values) % 2 != 0:
            values.append(((23*60 + 59), 'OUT'))
        tmp = []
        for i in range(0, len(values), 2):
            # IN, OUT 순서대로 들어있으므로 2개씩 잘라서 OUT에서 IN 시간 빼기
            tmp.append(int(values[i + 1][0]) - int(values[i][0]))
        minute[key] = sum(tmp) - fees[0] # 기본 시간 빼기
        if sum(tmp) - fees[0] < 0:
            minute[key] = 0
        cost[key] += fees[1] # 기본 요금 더하기
        if minute[key] > 0:
            cost[key] += (minute[key] // fees[2]) * fees[3] # 추가시간 계산
            if minute[key] % fees[2] != 0:
                cost[key] += fees[3]
    answer = list(map(func, sorted(cost.items()))) # 
    print(sorted(cost.items()))
    # print(record_dict)
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))