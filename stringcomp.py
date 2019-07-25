def compare_strings(a, b):
    """ Case insensitive string comparison in O(n) """
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i].upper() != b[i].upper():
            return False
    return True

while True:
    a = input("String A: ")
    b = input("String B: ")
    print(compare_strings(a, b))
