class BinaryTree:
    def __init__(self, rootobj):
        self.key = rootobj
        self.leftChild = None
        self.rightChild = None

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def insertLeft(self, newnode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newnode)
        else:
            node = BinaryTree(newnode)
            # 先把左子树给新节点组成的二叉树的左子树
            node.leftChild = self.leftChild
            # 然后再把新的二叉树做为左子树
            self.leftChild = node

    def insertRight(self, newnode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newnode)
        else:
            node = BinaryTree(newnode)
            # 先把左子树给新节点组成的二叉树的左子树
            node.rightChild = self.rightChild
            # 然后再把新的二叉树做为左子树
            self.rightChild = node

    def setrootVal(self, obj):
        self.key = obj

    def getrootVal(self):
        return self.key


l = []


# 递归:前序遍历
def pre_Order(tree):
    if tree:
        l.append(tree.getrootVal())
        pre_Order(tree.getLeftChild())
        pre_Order(tree.getRightChild())
    return l


# 递归:中序遍历
def in_Order(tree):
    if tree:
        in_Order(tree.getLeftChild())
        l.append(tree.getrootVal())
        in_Order(tree.getRightChild())
    return l


# 递归:后序遍历
def post_Order(tree):
    if tree:
        post_Order(tree.getLeftChild())
        post_Order(tree.getRightChild())
        l.append(tree.getrootVal())
    return l


# 循环遍历：前序
# 前序：中左右，每次先把当前遍历的节点cur打印，然后把右节点压栈（目的是为了判断左子节点的左子树是否为空，为空就弹栈再打印），
# 接着把当前节点指向左子节点。至于出栈的条件是当前节点cur为None就出栈
def preorderTraversal(tree):
    ordered_list = []
    stack = []
    cur = tree

    while cur or stack:
        if cur:
            ordered_list.append(cur.getrootVal())
            stack.append(cur.getRightChild())
            cur = cur.getLeftChild()
        else:
            cur = stack.pop()
    return ordered_list


# 循环遍历：中序
# 中序：左中右，当cur不为None，cur压栈，反之，出栈一个节点，打印栈节点当值，整个循环在stack和cur都为None都时候结束
def inorderTraversal(tree):
    ordered_list = []
    stack = []
    cur = tree
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.getLeftChild()
        else:
            cur = stack.pop()
            ordered_list.append(cur.getrootVal())
            cur = cur.getRightChild()
    return ordered_list


# 循环遍历：后序
# 后序：左右中，反过来就中右左，跟前序遍历(中左右)类似，只是把左右子树的顺序调换而已,输出的时候，倒转顺序。
def postorderTraversal(tree):
    ordered_list = []
    stack = []
    cur = tree
    while cur or stack:
        if cur:
            ordered_list.append(cur.getrootVal())
            stack.append(cur.getLeftChild())  # 左子节点入栈
            cur = cur.getRightChild()  # 调换为当前节点指向右子节点
        else:
            cur = stack.pop()
    return ordered_list[::-1]


t = BinaryTree(10)
t.insertLeft(6)
t.insertRight(14)
t.getLeftChild().insertLeft(4)
t.getLeftChild().insertRight(8)
t.getRightChild().insertLeft(12)
t.getRightChild().insertRight(16)


# print(pre_Order(t)) # [10, 6, 4, 8, 14, 12, 16]
# print(in_Order(t))  # [4, 6, 8, 10, 12, 14, 16]
# print(post_Order(t))# [4, 8, 6, 12, 16, 14, 10]

# print(preorderTraversal(t))  # [10, 6, 4, 8, 14, 12, 16]
# print(inorderTraveral(t))    # [4, 6, 8, 10, 12, 14, 16]
# print(postorderTraversal(t)) # [4, 8, 6, 12, 16, 14, 10]
