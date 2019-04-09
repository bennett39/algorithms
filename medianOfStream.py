from heapq import *

small = []
large = []

while True:
    try:
        num = int(input("Integer: "))
    except ValueError:
        continue
    if len(small) == len(large):
        heappush(large, -heappushpop(small, -num))
    else:
        heappush(small, -heappushpop(large, num))
    print(small, large)
    if len(small) == len(large):
        print("Median = ", float(large[0] - small[0]) / 2.0)
    else:
        print("Median = ", float(large[0]))
