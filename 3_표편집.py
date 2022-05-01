def solution(n, k, cmd):
    answer = ''
    arr = [i for i in range(n)]
    rm_list = []
    for c in cmd:
        if c[0] == 'D':
            c = c.split()
            k += int(c[1])
        elif c[0] == 'U':
            c = c.split()
            k -= int(c[1])
        elif c[0] == 'C':
            rm = arr[k]
            rm_list.append((k, rm))
            arr = arr[0:k] + arr[k + 1:]
            if k == len(arr):
                k = len(arr) - 1
            # arr.remove(rm)

        elif c[0] == 'Z':
            cur = arr[k]
            last = rm_list.pop()
            arr = arr[0:last[0]] + [last[1]] + arr[last[0]:]
            # k = arr.index(cur)
            if k + 1 < len(arr) and arr[k + 1] == cur: k = k+1
            elif k - 1 > 0 and arr[k - 1] == cur: k = k - 1
    answer = ['X' for _ in range(n)]
    for i in arr:
        answer[i] = 'O'
    return ''.join(answer)

class Node:
    def __init__(self):
        self.prev = -1
        self.next = -1
        self.rm = False

def solution2(n, k, cmd):
    node = [Node() for _ in range(n)]
    rm_list = []
    cur = k
    for i in range(n - 1):
        node[i + 1].prev = i
        node[i].next = i + 1
    for c in cmd:
        c = c.split()
        if c[0] == 'U':
            # k -= int(c.split()[1])
            for i in range(int(c[1])):
                cur = node[cur].prev
        elif c[0] == 'D':
            # k += int(c.split()[1])
            for i in range(int(c[1])):
                cur = node[cur].next
        elif c[0] == 'C':
            # rm = node[k]
            node[cur].rm = True
            rm_list.append(cur)
            next = node[cur].next
            prev = node[cur].prev
            if prev != -1: # 이전 노드가 있으면
                node[prev].next = next #이전 노드의 next를 현재 노드의 next 로 변경
            if next != -1: # 다음 노드가 있으면
                node[next].prev = prev
                cur = next
            else:
                cur = prev
            
        elif c[0] == 'Z':
            rm = rm_list.pop()
            node[rm].rm = False
            prev = node[rm].prev
            next = node[rm].next
            if prev != -1:
                node[prev].next = rm
            if next != -1:
                node[next].prev = rm
    answer = ''
    for i in range(n):
        if node[i].rm:
            answer += 'X'
        else:
            answer += 'O'
    return answer


print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))