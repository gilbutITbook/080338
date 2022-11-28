class node:
    def __init__(self, info):
        self.number = info[2]
        self.data = info[:2]
        self.right = None
        self.left = None
        
def addnode(root, info):
    if info[0] > root.data[0]:
        if not root.right: root.right = node(info)
        else: addnode(root.right, info)
    elif info[0] < root.data[0]:
        if not root.left: root.left = node(info)
        else: addnode(root.left, info)
        
def preorder(root, order):
    if root != None:
        order.append(root.number)
        preorder(root.left, order)
        preorder(root.right, order)

def postorder(root, order):
    if root != None:
        postorder(root.left, order)
        postorder(root.right, order)
        order.append(root.number)

def solution(nodeinfo):
    nodeinfo = [[*info, idx + 1] for idx, info in enumerate(nodeinfo)]
    nodeinfo = sorted(nodeinfo, key=lambda x: x[1], reverse=True)

    root = node(nodeinfo[0])
    
    for info in nodeinfo[1:]:
        addnode(root, info)

    preorderList = []
    preorder(root, preorderList)

    postorderList = []
    postorder(root, postorderList)

    return [preorderList, postorderList]

