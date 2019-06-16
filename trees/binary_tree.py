"""
二叉搜索树
"""


class TreeNode(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left: TreeNode = left
        self.right: TreeNode = right

    def find_min(self):
        temp = self
        while temp.left:
            temp = temp.left

        return temp


def insert_tree_node(node, element):
    if node is None:
        node = TreeNode(element)
    else:
        if element < node.element:
            node.left = insert_tree_node(node.left, element)
        elif element > node.element:
            node.right = insert_tree_node(node.right, element)

    return node


def delete_tree_node(node, element):
    if node is None:

        return False
    else:
        if element < node.element:
            node.left = delete_tree_node(node, element)
        elif element > node.element:
            node.right = delete_tree_node(node, element)
        else:
            # 找到节点
            # 1. 被删除的节点有左右两个节点
            if node.left and node.right:
                temp = node.right.find_min()
                node.element = temp.element
                node.right = delete_tree_node(node.right, temp.element)
            else:
                if node.left:   # 只有左节点
                    node = node.left
                else:           # 只有右节点，或没有节点
                    node = node.right

        return node


class Tree(object):
    def __init__(self):
        self.root: TreeNode = None

    def is_empty(self):

        return self.root is None

    def insert(self, element):
        """
        插入数据
        """
        if self.is_empty():
            self.root = TreeNode(element)
        else:
            self.root = insert_tree_node(self.root, element)

    def delete(self, element):
        if self.is_empty():
            return False
        else:
            return delete_tree_node(self.root, element)