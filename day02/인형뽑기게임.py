def solution(board, moves):
    answer = 0
    basket = []
    # board
    #[[0,0,0,0,0],
    # [0,0,1,0,3],
    # [0,2,5,0,1],
    # [4,2,4,4,2],
    # [3,5,1,3,1]]
    for m in moves:
        for i in range(len(board)):
            # print('basket: ', basket)
            if board[i][m - 1] != 0:
                if len(basket) == 0 or basket[len(basket) - 1] != board[i][m - 1]:
                    basket.append(board[i][m - 1])
                else:
                    answer += 2
                    basket.pop()

                board[i][m - 1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))