"""
平衡二叉树
"""


class TreeNode(object):
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right
        self.height = 0

    def __str__(self):
        return str(self.element)


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, element):
        self.root = insert_tree_node(self.root, element)


def get_height(node):
    if node:
        return node.height
    else:
        return 0


def single_left_rotation(node):
    """
    左旋，条件：
    1. 有左节点
    2. 插入节点在左节点左边
    :param node:
    :return:
    """
    left: TreeNode = node.left
    node.left = left.right
    left.right = node

    node.height = max(get_height(node.left), get_height(node.right)) + 1
    left.height = max(get_height(node), get_height(left.left)) + 1

    return left


def single_right_rotation(node):
    """
    右旋，条件：
    1. 有右节点
    2. 插入节点在右节点右边
    :param node:
    :return:
    """
    right: TreeNode = node.right
    node.right = right.left
    right.left = node

    node.height = max(get_height(node.left), get_height(node.right)) + 1
    right.height = max(get_height(node), get_height(right.right)) + 1

    return right


def double_left_right_rotation(node):
    """
    左右双旋，条件
    1. 有左节点
    2. 左节点有右节点
    3. 插入节点在左节点右边
    :param node:
    :return:
    """
    node.left = single_right_rotation(node.left)

    return single_left_rotation(node)


def double_right_left_rotation(node):
    """
    右左双旋，条件
    1. 有右节点
    2. 右节点有左节点
    3. 插入节点在右节点左边
    :param node:
    :return:
    """
    node.right = single_left_rotation(node.right)

    return single_right_rotation(node)


def insert_tree_node(node, element):
    if node is None:
        node = TreeNode(element)
    elif element < node.element:
        node.left = insert_tree_node(node.left, element)

        if get_height(node.left) - get_height(node.right) == 2:
            if element < node.left.element:
                node = single_left_rotation(node)
            else:
                node = double_left_right_rotation(node)
    elif element > node.element:
        node.right = insert_tree_node(node.right, element)

        if get_height(node.right) - get_height(node.left) == 2:
            if element > node.right.element:
                node = single_right_rotation(node)
            else:
                node = double_right_left_rotation(node)
    else:
        pass

    node.height = max(get_height(node.left), get_height(node.right)) + 1

    return node
