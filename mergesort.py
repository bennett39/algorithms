def merge(a, b):
    c = []
    while a and b:
        if a[0] < b[0]:
            c += a[0],
            a = a[1:]
        else:
            c += b[0],
            b = b[1:]
    while a:
        c += a[0],
        a = a[1:]
    while b:
        c += b[0],
        b = b[1:]
    return c


def mergesort(array):
    n = len(array)
    if n < 2:
        return array
    return merge(mergesort(array[:n//2]), mergesort(array[n//2:]))

unsorted = [3, 1, 4, 7, 2, 9, 6]
assert mergesort(unsorted) == sorted(unsorted)
