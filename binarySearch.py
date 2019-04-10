def binary_search(sorted_list, val):
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        print(f"lo: {lo} \thi: {hi}\tmid: {mid}\tcomp: {sorted_list[mid]}")
        if sorted_list[mid] == val:
            return mid
        elif sorted_list[mid] > val:
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

test = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 22, 23, 25, 43, 45, 65,
        66, 78, 87, 88, 96, 97, 99, 100, 120, 240, 600, 789, 999]
