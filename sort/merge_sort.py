def merge_sort(lyst):
    copy_buffer = [0] * len(lyst)
    merge_sort_helper(lyst, copy_buffer, 0, len(lyst) - 1)


def merge_sort_helper(lyst, copy_buffer, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort_helper(lyst, copy_buffer, left, middle)
        merge_sort_helper(lyst, copy_buffer, middle + 1, right)
        merge(lyst, copy_buffer, left, middle, right)


def merge(lyst, copy_buffer, left, middle, right):
    i1 = left
    i2 = middle + 1

    for i in range(left, right + 1):
        print(i1, i2, right)
        if i1 > middle:
            copy_buffer[i] = lyst[i2]
            i2 += 1
        elif i2 > right:
            copy_buffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copy_buffer[i] = lyst[i1]
            i1 += 1
        else:
            copy_buffer[i] = lyst[i2]
            i2 += 1

    for i in range(left, right + 1):
        lyst[i] = copy_buffer[i]


if __name__ == '__main__':
    import random

    test = list(range(10))
    random.shuffle(test)
    merge_sort(test)
    print(test)

