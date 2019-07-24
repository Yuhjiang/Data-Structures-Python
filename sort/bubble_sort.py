def bubble_sort(lyst):
    """
    外围循环从n开始
    内围循环从0开始，逐一把大值向后移动
    """
    i = len(lyst) - 1
    while i > 0:
        for j in range(0, i):
            if lyst[j] > lyst[j+1]:
                lyst[j], lyst[j+1] = lyst[j+1], lyst[j]
        i -= 1


if __name__ == '__main__':
    import random

    test = list(range(10))
    random.shuffle(test)
    bubble_sort(test)
    print(test)