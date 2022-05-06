def solution(triangle):
    total = [[t for t in tt] for tt in triangle]
    max_num = 0
    #     7
    #    3 8
    #   8 1 0
    #  2 7 4 4
    # 4 5 2 6 5
    # 이런 삼각형에서 꼭대기부터 바닥까지
    # 바로 아래 왼쪽이나 오른쪽 원소로 값을 더했을 때 나오는 최댓값을 구하기
    for tri in range(0, len(triangle) - 1): # 0 ~ n - 1 번째 줄
        for tr in range(0, len(triangle[tri])):
            # 윗줄에서 아랫줄로 누적 합
            # 왼쪽, 오른쪽에 하나씩 더해줌
            # 부모가 두개인 경우, 왼쪽 부모 더했을 때, 오른쪽 부모 더했을 때 최대값 구함
            if triangle[tri + 1][tr] < total[tri + 1][tr] + triangle[tri][tr]:
                triangle[tri + 1][tr] = total[tri + 1][tr] + triangle[tri][tr]
            if triangle[tri + 1][tr + 1] < total[tri + 1][tr + 1] + triangle[tri][tr]:
                triangle[tri + 1][tr + 1] = total[tri + 1][tr + 1] + triangle[tri][tr]
    # 바닥에 있는 원소들 중 최댓값 구하기
    for tri in range(len(triangle[len(triangle) - 1])):
        max_num = max(max_num, triangle[len(triangle) - 1][tri])
    return max_num

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	))