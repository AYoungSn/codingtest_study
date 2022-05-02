class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def maketree(nodeinfo, dic):
    # nodeinfo는 y 축을 기준으로 정렬된 상태
    if len(nodeinfo) == 0:
        return None
    
    root = tuple(nodeinfo[0])
    idx = dic[root]

    nodeinfo.pop(0) # root 원소를 pop
    lefts = []
    rights = []
    # 주어진 node 들 중 root를 기준으로 왼쪽 / 오른쪽 서브트리 노드들을 분리
    for node in nodeinfo:
        if node[0] < root[0]:
            lefts.append(node)
        elif node[0] > root[0]:
            rights.append(node)
    del dic[root]
    # 주어진 node들 중의 root(root 값, 왼쪽 서브트리, 오른족 서브트리)
    # maketree(lefts, dic) : 왼쪽 서브트리를 만들어서 리턴
    # maketree(rights, dic): 오른쪽 서브트리를 만들어서 리턴
    return Tree(idx, maketree(lefts, dic), maketree(rights, dic))

def preorder(tree, li):
    if tree == None:
        return 
    li.append(tree.data)
    preorder(tree.left, li)
    preorder(tree.right, li)
    return li

def postorder(tree, li):
    if tree == None:
        return
    postorder(tree.left, li)
    postorder(tree.right, li)
    li.append(tree.data)
    return li


def solution(nodeinfo):
    dic = {}
    for i, x in enumerate(nodeinfo): # dic[(x, y)] = data (index + 1)
        dic[tuple(x)] = i + 1
    print(nodeinfo)
    # key: nodeinfo 원소의 y 좌표를 기준으로 정렬
    # reverse: 내림차순 정렬
    nodeinfo.sort(key=lambda x: x[1], reverse=True)
    tree = maketree(nodeinfo, dic)

    return [preorder(tree, []), postorder(tree, [])]

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))