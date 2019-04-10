from timeit import default_timer
from quicksort import quicksort
from mergesort import mergesort

test_data = [
        5, 2, 4, 6, 9, 1, 4, 2, 7, 9, 1,
        2, 9, 3, 1, 7, 4, 2, 8, 7, 3, 5,
        6, 2, 7, 3, 1, 1, 6, 9, 3, 5, 8,
        2, 7, 4, 1, 3, 9, 8, 5, 3, 5, 7,
        2, 8, 4, 6, 9, 1, 4, 5, 3, 4, 6
]

standard_start = default_timer()
s = sorted(test_data)
standard_end = default_timer()


quick_start = default_timer()
n = len(test_data)
q = quicksort(test_data, 0, n)
quick_end = default_timer()

merge_start = default_timer()
m = mergesort(test_data)
merge_end = default_timer()

assert q == m == s
print(f"Standard: {standard_end - standard_start}")
print(f"Quicksort: {quick_end - quick_start}")
print(f"Mergesort: {merge_end - merge_start}")
