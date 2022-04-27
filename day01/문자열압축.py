def solution(s):
    answer = len(s)
    res = ''
    for i in range(1, len(s)):
        j = 0
        while j < len(s):
            ch = s[j: j + i]
            count = 1
            for k in range(j + i*2, len(s) + 1, i):
                if ch == s[k - i: k]:
                    count += 1
                else:
                    break
            if count == 1:
                res += ch
                j += i
            else:
                res += str(count) + ch
                j += i * count
        if answer > len(res):
            answer = len(res)
        res = ''
    return answer