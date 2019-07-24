def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst) - 1)


def quick_sort_helper(lyst, left, right):
    if left < right:
        pivot_location = partition(lyst, left, right)
        quick_sort_helper(lyst, left, pivot_location - 1)
        quick_sort_helper(lyst, pivot_location + 1, right)


def partition(lyst, left, right):
    # 选取pivot，原则是left, right, middle排序
    middle = (left + right) // 2
    pivot = lyst[middle]

    # pivot放到最后，前面排好序了之后，再放回去
    lyst[right], lyst[middle] = lyst[middle], lyst[right]
    boundary = left

    for i in range(left, right):
        if lyst[i] < pivot:
            lyst[boundary], lyst[i] = lyst[i], lyst[boundary]
            boundary += 1
    lyst[right], lyst[boundary] = lyst[boundary], lyst[right]

    return boundary


if __name__ == '__main__':
    import random

    test = list(range(10))
    random.shuffle(test)
    quick_sort(test)
    print(test)
