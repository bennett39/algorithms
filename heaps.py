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
    if len(small) == len(large):
        print(float(large[0] - small[0]) / 2.0)
    else:
        print(float(large[0]))
    print(small, large)
