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
            self.leftChild = newnode
        else:
            node = BinaryTree(newnode)
            # 先把左子树给新节点组成的二叉树的左子树
            node.leftChild = self.leftChild
            # 然后再把新的二叉树做为左子树
            self.leftChild = node

    def insertRight(self, newnode):
        if self.rightChild == None:
            self.rightChild = newnode
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


# 递归:前序遍历
def pre_Order(tree):
    #先打印根结点
    print(tree.getrootVal)

    if tree.leftChild:
        pre_Order(tree.getLeftChild())
    if tree.rightChild:
        pre_Order(tree.getRightChild())


# 递归:中序遍历
def in_Order(tree):
    if tree:
        in_Order(tree.getLeftChild())
        print(tree.getrootVal())
        in_Order(tree.getRightChild())


# 递归:后序遍历
def post_Order(tree):
    if tree:
        post_Order(tree.leftChild)
        post_Order(tree.rightChild)
        print(tree.getrootVal)