MIN_DATA = -65536


class Heap(object):
    def __init__(self):
        self.data = [MIN_DATA]      # 第一个位置不作任何用途，堆的数据从1开始
        self.size = 0

    def insert(self, element):
        # 在某尾建一个空穴，然后执行上滤操作去填空穴
        self.size += 1
        self.data.append(element)
        i = self.size

        while self.data[i // 2] > element:
            self.data[i] = element
            i //= 2
        self.data[i] = element

    def is_empty(self):
        return self.size == 0

    def delete(self):
        # 根节点为空穴，子节点中较小值下滤
        if self.is_empty():
            return False
        result = self.data.pop(1)
        self.size -= 1
        parent = 1
        x = self.data[self.size]

        while parent * 2 <= self.size:
            child = parent * 2

            if child < self.size and self.data[child] > self.data[child + 1]:
                child = child + 1

            if self.data[child] < x:
                self.data[parent] = self.data[child]
            else:
                break
            parent = child
        self.data[parent] = x

        return result

    def percdown(self, p):
        # 指定位置下滤
        x = self.data[p]
        while p * 2 <= self.size:
            child = p * 2
            if child < self.size and self.data[child] > self.data[child + 1]:
                child = child + 1

            if self.data[child] < x:
                self.data[p] = self.data[child]
            else:
                break
            p = child
        self.data[p] = x

    def build_heap(self, data):
        self.data += data
        self.size = len(data)
        for p in range(1, self.size // 2 + 1)[::-1]:
            self.percdown(p)


if __name__ == '__main__':
    heap = Heap()
    heap.build_heap(list(range(6)[::-1]))

    print(heap.data)