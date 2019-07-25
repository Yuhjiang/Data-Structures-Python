from . import log


@log
def selection_sort(lyst):
    """
    1.外围循环从0开始，设为i
    2.内层循环从i+1开始，设为j，寻找i以后的最小值，最后替换到i的位置
    """
    for i in range(len(lyst) - 1):
        min_index = i
        for j in range(i + 1, len(lyst)):
            if lyst[j] < lyst[min_index]:
                min_index = j
        lyst[i], lyst[min_index] = lyst[min_index], lyst[i]


if __name__ == '__main__':
    import random

    test = list(range(10))
    random.shuffle(test)
    selection_sort(test)
    print(test)