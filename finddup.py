a = [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]

def find_duplicate_sorted(array):
    for i in range(1, len(array)):
        if array[i] == array[i-1]:
            return array[i]
    return 0

def find_duplicate_set(array):
    return sum(array) - sum(set(array))

print(find_duplicate_sorted(a))
print(find_duplicate_set(a))
