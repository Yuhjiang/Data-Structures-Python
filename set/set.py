"""
集合
"""


class Set(object):
    def __init__(self, size):
        self.data = [-1] * size

    def find(self, element):
        """
        寻找element，利用路径压缩
        :param element:
        :return: 父节点
        """
        if self.data[element] < 0:  # 找到
            return element
        else:
            return self.find(self.data[element])

    def union(self, root1, root2):
        """
        联结两个字集合，小的集合合并到大集合里
        :param root1: 集合1
        :param root2: 集合2
        """
        if self.data[root1] < self.data[root2]:     # 集合1小于集合2
            self.data[root2] += self.data[root1]
            self.data[root1] = root2                # 更新root1的父节点
        else:
            self.data[root1] += self.data[root2]
            self.data[root2] = root1

