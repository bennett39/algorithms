def quicksort(unsorted, lo, hi):
    if hi - lo < 2:
        return unsorted
    pivot = unsorted[lo]
    bumper = lo
    for i in range(lo, hi):
        if unsorted[i] < pivot:
            bumper += 1
            unsorted[i], unsorted[bumper] = unsorted[bumper], unsorted[i]
    unsorted[lo], unsorted[bumper] = unsorted[bumper], unsorted[lo]
    quicksort(unsorted, lo, bumper)
    quicksort(unsorted, bumper+1, hi)
    return unsorted


unsorted = [5, 9, 2, 3, 8, 3, 1]
test = [1, 2, 3, 3, 5, 8, 9]

assert quicksort(unsorted, 0, len(unsorted)) == test
