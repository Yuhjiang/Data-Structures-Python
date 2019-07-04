"""
堆
1. 采用list形式构建堆
"""
MIN_DATA = -65536


class Heap(object):
    def __init__(self):
        self.data = [MIN_DATA]
        self.size = 0

    def insert(self, element):
        # 在堆最后一个位置放入空位
        self.data.append(element)
        self.size += 1
        i = self.size   # 标记位置

        while element < self.data[i//2]:
            # 上滤操作
            self.data[i] = self.data[i//2]
            i /= 2
        self.data[i] = element

        return True

    def is_empty(self):

        return self.size == 0

    def delete(self):
        if self.is_empty():
            return False

        # 取出根节点存放的小值
        result = self.data[1]
        self.size -= 1
        # 最小堆的第二层开始下滤
        x = self.data[self.size]
        parent = 1
        while parent * 2 < self.size:
            child = parent * 2
            # child指向节点里较小点
            if child != self.size and self.data[child + 1] < self.data[child]:
                child += 1

            if x <= self.data[child]:    # 找到合适的位置
                break
            else:
                self.data[parent] = self.data[child]
        self.data[parent] = x

        return result

    def percdown(self, p):
        """
        在P位置执行下滤
        :param p: 初始堆的根
        """
        x = self.data[p]
        parent = p

        while parent * 2 < self.size:
            child = parent * 2
            if child != self.size and self.data[child + 1] < self.data[child]:
                child += 1

            if x <= self.data[child]:
                break
            else:
                self.data[parent] = self.data[child]
        self.data[parent] = x

    def build_heap(self, data):
        self.data = data
        self.size = len(data)

        for i in range(1, self.size // 2 + 1)[::-1]:
            self.percdown(i)
