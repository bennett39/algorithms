a = [1, 2, 3, 4, 5, 7, 8, 9, 10]

def find_missing_sorted(array):
    # optionally, sort the array here - n log n
    for i in range(1, len(array)): # O(n)
        if array[i] != array[i-1] + 1: # O(1)
            return array[i-1] + 1
    return 0

def find_missing_unsorted(array):
    # Only one value missing
    arr_max, arr_min = max(array), min(array) # O(n), O(n)
    expected = sum([x for x in range(arr_min, arr_max + 1)]) # O(2n)
    actual = sum(array) # O(n)
    return expected - actual # O(1)

print(find_missing_sorted(a))
print(find_missing_unsorted(a))
