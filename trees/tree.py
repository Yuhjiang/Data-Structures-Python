class TreeNode(object):
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self, root: TreeNode):
        self.root = root

    def preorder_traversal(self, node: TreeNode):
        """
        先序遍历
        """
        if node:
            print(node.element)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node: TreeNode):
        """
        后序遍历
        """
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.element)

    def inorder_traversal(self, node: TreeNode):
        """
        中序遍历
        """
        if node:
            self.inorder_traversal(node.left)
            print(node.element)
            self.inorder_traversal(node.right)

    def level_traversal(self, node: TreeNode):
        """
        层序遍历
        """
        queue = []
        if node:
            queue.append(node)

        while queue:
            temp = queue.pop(0)      # 弹出节点，并把它的子节点入队列
            print(temp.element)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    def invert(self, node: TreeNode):
        """
        树的左右节点翻转
        """
        node.left, node.right = node.right, node.left
        if node.left:
            self.invert(node.left)
        if node.right:
            self.invert(node.right)

    def tree_search(self, node: TreeNode, element):
        """
        二叉树搜索
        """
        if node.element == element:
            return node
        if node.left:
            return self.tree_search(node.left, element)
        if node.right:
            return self.tree_search(node.right, element)

    def bst_search(self, node: TreeNode, element):
        """
        平衡二叉树搜索
        """
        if node is None:
            return None

        if node.element == element:
            return node
        elif node.element > element:
            return self.bst_search(node.left, element)
        else:
            return self.bst_search(node.right, element)