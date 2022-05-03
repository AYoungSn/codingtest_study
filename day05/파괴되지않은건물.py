# 누적 합 구하기
def solution(board, skill):
    answer = 0
    arr = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            arr[r1][c1] -= degree # 계산할 시작 위치에 값 추가
            arr[r1][c2 + 1] += degree # 계산할 범위의 오른쪽 끝 + 1 에 표시
            arr[r2 + 1][c1] += degree # 계산 범위의 아래쪽 끝 + 1 에 뒤쪽에 더이상 더해지지 않도록
            arr[r2 + 1][c2 + 1] -= degree # 계산 범위의 행 + 1, 열 + 1
        else:
            arr[r1][c1] += degree
            arr[r1][c2 + 1] -= degree
            arr[r2 + 1][c1] -= degree
            arr[r2 + 1][c2 + 1] += degree
    
    for c in range(len(board[0])):
        # arr[0][c] += arr[0][c]
        for r in range(1, len(board)):
            arr[r][c] += arr[r - 1][c]
    for r in range(len(board)):
        # board[r][0] += arr[r][0]
        for c in range(1, len(board[0])):
            arr[r][c] += arr[r][c - 1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += arr[i][j]
    print(board)
    
    for c in board:
        for r in c:
            if r > 0:
                answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))

print(solution([[1,2,3],[4,5,6],[7,8,9]],
[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))