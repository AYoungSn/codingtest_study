# greedy
def solution(number, k):
    answer = ''
    arr = []
    tmp = k
    for num in number:
        if not arr: # arr 이 비어있으면 일단 새로 push()
            arr.append(num) 
            continue
        if k > 0: # 뺄 갯수가 남아있으면 현재 숫자보다 스택의 마지막 원소가 작은지 체크
            while k > 0 and arr and arr[-1] < num:
                if arr[-1] < num: # 현재 숫자보다 마지막 원소가 작으면 뺌
                    arr.pop()
                    k -= 1 # 뺀 갯수 차감
        arr.append(num)

    return ''.join(arr[:len(number) - tmp])

print(solution("1924", 2))
print(solution("1231234", 3))