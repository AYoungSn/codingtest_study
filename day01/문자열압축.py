def solution(s):
    answer = len(s)
    res = ''
    for i in range(1, len(s)): # 문자열을 i 개로 자름
        j = 0
        while j < len(s): # 0번부터 i 개씩 잘라보기
            ch = s[j: j + i]
            count = 1
            for k in range(j + i*2, len(s) + 1, i):
                if ch == s[k - i: k]:
                    count += 1
                else:
                    break
            if count == 1: # i개로 잘랐을 때 뒤에 겹치는게 없는 경우
                res += ch
                j += i # 현재 문자열 바로 뒤부터 다시 체크
            else:
                res += str(count) + ch
                j += i * count # 겹치는 문자열만큼 빼고 체크
        if answer > len(res):
            answer = len(res)
        res = ''
    return answer

def solution2(s):
    answer = len(s)
    if answer <= 2:
        return answer
    for i in range(1, len(s) // 2 + 1): # 문자열 쪼개는 단위 -> 1 ~ (len(s) / 2)
        j = 0
        result = ''
        while j < len(s): # j 번째 위치부터 i 개로 짤라보기
            ch = s[j: j + i]
            count = 1
            for k in range(j + i, len(s), i): # ch 문자열이 반복되는게 있는지 체크
                if ch == s[k:k + i]:
                    count += 1
                else:
                    break
            if count != 1:
                result += str(count) + ch # 문자열 압축
            else:
                result += ch #현재 문자열 추가
            j += i * count
        if len(result) < answer:
            answer = len(result)
    return answer