from copy import deepcopy

# 0.5

def solution(rc, operations):
    answer = deepcopy(rc)
    for op in operations:
        if op == "ShiftRow":
            tmp = rc.pop()
            # print('rc,pop', rc, tmp)
            rc = [tmp] + rc[0:]
            # print('sh', rc)
            answer = deepcopy(rc)
        else:
            # 첫번째 행의 1번째 열부터 n - 1 -> 2 ~ n - 1
            for j in range(1, len(rc[0])):
                # print(j)
                # print(rc)
                answer[0][j] = rc[0][j - 1]
            # 가장 오른쪽 행의 1번째 행부터 n-1 -> 2 ~ n
            for j in range(1, len(rc)):
                answer[j][len(rc[0]) - 1] = rc[j - 1][len(rc[0]) - 1]

            for j in range(1, len(rc[0])):
                answer[len(rc) - 1][j - 1] = rc[len(rc) - 1][j]

            for j in range(len(rc) - 1):
                answer[j][0] = rc[j + 1][0]
            rc = deepcopy(answer)

    return rc

# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]],["Rotate", "ShiftRow"]))
# print(solution([[8, 6, 3], [3, 3, 7], [8, 4, 9]],	["Rotate", "ShiftRow", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],	["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))