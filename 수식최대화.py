from copy import deepcopy
import itertools

def oper(a, b, op):
    if op == '+':
        return int(a) + int(b)
    elif op == '-':
        return int(a) - int(b)
    elif op == '*':
        return int(a) * int(b)

def solution(expression):
    answer = 0
    start = 0
    arr = []
    for i in range(len(expression)):
        if i < len(expression) - 1 and not expression[i].isdigit():
            arr.append(expression[start:i])
            if i < len(expression) - 1:
                arr.append(expression[i])
            start = i + 1
    arr.append(expression[start:])
    for op in itertools.permutations(["*", "-", "+"], 3):
        tmp = deepcopy(arr)
        for o in op:
            i = 0
            while i < len(arr):
                if arr[i] == o:
                    print(i, arr)
                    arr[i] = str(oper(arr[i - 1], arr[i + 1], arr[i]))
                    arr.pop(i - 1)
                    arr.pop(i)
                    i = 0
                i+=1
        answer = max(abs(int(arr[0])), answer)
        arr = tmp

    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))