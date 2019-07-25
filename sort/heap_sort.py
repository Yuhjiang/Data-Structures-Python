"""
堆排序
先建立一个最大堆
然后逐个删除根节点
删除的意思是将根节点和最后的节点交换，然后对新的根节点做下滤
"""
import random
from . import log


def percdown(data, p, size):
    x = data[p]

    left_child = lambda i: i * 2 + 1
    while left_child(p) < size:
        child = left_child(p)

        if child < size - 1 and data[child] < data[child+1]:
            child = child + 1

        if data[child] > x:
            data[p] = data[child]
        else:
            break
        p = child
    data[p] = x


@log
def heap_sort(data):
    size = len(data)

    for p in range(size // 2)[::-1]:
        percdown(data, p, size)

    for s in range(size)[::-1]:
        data[s], data[0] = data[0], data[s]
        percdown(data, 0, s)


if __name__ == '__main__':
    test = list(range(10))
    random.shuffle(test)
    heap_sort(test)
    print(test)