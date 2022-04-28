import itertools


def solution(orders, course):
    answer = []
    orders = list(map(set, orders))
    order_combinations = []
    menu_dict = {}
    for cnt in course:
        menu_dict[cnt] = [] # 메뉴 갯수: [], 메뉴갯수: [] 형태로 만들기
    for menu in orders: # 메뉴 하나씩 순회
        size = len(menu)
        for cnt in course: # 메뉴 갯수
            # 메뉴 갯수가 course에 적힌 수보다 크거나 같을 때만 체크
            if cnt < size: # 주문한 메뉴의 개수가 조합할 메뉴개수보다 클때
                # 주문한 메뉴를 조합할 메뉴 개수만큼의 튜플로 생성 cnt=2, items[(A, B), (C, D),,]
                items = list(map(''.join, list(itertools.combinations(sorted(menu), cnt))))
                order_combinations += items
            elif cnt == size:
                order_combinations.append(''.join(sorted(menu))) # 주문한 메뉴들을 sorted 해서 추가해야 CA -> AC 로 됨

    # print(order_combinations)

    for item in set(order_combinations): # 리스트를 집합으로 만들어서 중복 제거
        cnt = order_combinations.count(item) # 조합에서 item 이 나타난 횟수
        if cnt >= 2: # item 이 두번이상 나타난 경우
            menu_dict[len(item)].append((cnt, item)) # dict 
    
    for c in menu_dict.values():
        max_cnt = 0
        arr = []
        for k, v in c:
            if max_cnt < k:
                max_cnt = k
                arr = [v]
            elif max_cnt == k:
                arr.append(v)
        answer += arr
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))