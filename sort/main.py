from sort.quick_sort import quick_sort
from sort.heap_sort import heap_sort
from sort.bubble_sort import bubble_sort
from sort.insertion_sort import insertion_sort
from sort.selection_sort import selection_sort
from sort.merge_sort import merge_sort


data = list(range(10000)[::-1])
quick_sort(data)
data = list(range(10000)[::-1])
heap_sort(data)
data = list(range(10000)[::-1])
bubble_sort(data)
data = list(range(10000)[::-1])
insertion_sort(data)
data = list(range(10000)[::-1])
selection_sort(data)
data = list(range(10000)[::-1])
merge_sort(data)

