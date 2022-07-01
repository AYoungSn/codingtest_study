from collections import defaultdict

def solution(tickets):
    answer = []
    path = defaultdict(list)
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])
    for key in path.keys():
        path[key].sort(reverse=True)
    print(path)
    stack = ['ICN']
    while stack:
        top = stack[-1]
        if not path[top]:
            answer.append(stack.pop())
        else:
            stack.append(path[top].pop())
    print(stack)
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))