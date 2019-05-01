a = [12, 45, 77, 23, 345, 999, 987, 23, 5]

def find_max(array):
    maximum = float('-inf')
    for val in array:
        if val > maximum:
            maximum = val
    return maximum

print(find_max(a))
