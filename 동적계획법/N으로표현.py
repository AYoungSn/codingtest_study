def solution(N, number):
    answer = 0
    if N == number:
        return 1
    
    s = [set() for _ in range(8)]

    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i)) # 1{N}, 2{NN}, 3{NNN}

    for i in range(1,8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]: # i - j - 1 번째 인덱스에 들어있는 집합 원소 순회
                    # print(s[i - j - 1])
                    print(op1, op2)
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    print(s)
    return answer

print(solution(5, 12))
print(solution(2, 11))