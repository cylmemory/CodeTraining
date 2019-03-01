class BinaryTree:
    def __init__(self, nodevalue):
        self.data = nodevalue
        self.leftchild = None
        self.rightchild = None


class Solution:
    def reConstructBinaryTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        if set(preorder) != set(inorder):
            return None
        root = BinaryTree(preorder[0])  # 先获取根结点也就是preorder第一个元素
        inorder_index = inorder.index(preorder[0])  # 在inorder中找个这个元素的下标号，左边为左子树，右边为右子树

        root.leftchild = self.reConstructBinaryTree(preorder[1:inorder_index+1], inorder[:inorder_index])  # 左子树递归
        root.rightchild = self.reConstructBinaryTree(preorder[inorder_index+1:], inorder[inorder_index+1:])  # 右子树递归

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
s = Solution()
newTree = s.reConstructBinaryTree(preorder, inorder)