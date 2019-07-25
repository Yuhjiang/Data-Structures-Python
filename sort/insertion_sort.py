from . import log


@log
def insertion_sort(lyst):
    """
    假设前i项已经排好序，把第i+1项插入前面排好序的数组里
    """
    for i in range(1, len(lyst)):
        data_to_insert = lyst[i]
        j = i - 1
        while j >= 0:
            if lyst[j] > data_to_insert:
                lyst[j+1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j+1] = data_to_insert


if __name__ == '__main__':
    import random

    test = list(range(10))
    random.shuffle(test)
    insertion_sort(test)
    print(test)