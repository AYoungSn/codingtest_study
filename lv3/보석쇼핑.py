from collections import defaultdict


def solution2(gems): # 시간초과
    n = len(set(gems))
    min_count = len(gems) # gems 배열의 최대 크기
    min_start = 1
    min_end = len(gems)
    for start in range(0, len(gems) - n + 1):
        arr = gems[start:start + n]
        gem_set = set(arr)
        end = start + n
        count = len(arr)
        while end < len(gems) and len(gem_set) != n:
            gem_set.add(gems[end])
            count += 1
            end += 1
            if count >= min_count:
                break
            
        if len(gem_set) == n and count < min_count:
            min_start = start + 1
            min_end = end
            min_count = count
            if count == n:
                break

    answer = [min_start, min_end]
    return answer

def solution(gems): #시간 내에 해결
    gems_set = set(gems)
    gems_dict = defaultdict(lambda: 0)
    kind = len(gems_set)
    l , r = 0, 0
    answer = [0, 0]
    gems_len = len(gems)
    length = len(gems) + 1
    while True:
        s = len(gems_dict)
        if l == gems_len: # 바로 아래 if 문에서 gems[l]에 접근하기 전에 유효성 체크
            break
        if s == kind:
            if r - l - 1 < length:
                length = r - l - 1
                answer[0] = l + 1
                answer[1] = r
            
            gems_dict[gems[l]] -= 1
            if gems_dict[gems[l]] == 0:
                del gems_dict[gems[l]]
            l += 1
            continue
        if r == gems_len:# 바로 아래 if 문에서 gems[r]에 접근하기 전에 유효성 체크
            break
        if s != kind:
            gems_dict[gems[r]] += 1
            r += 1
            continue

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA", "XYZ", "XYZ", "XYZ"]))