import collections

q = collections.deque()
q.append('a')
q.appendleft('b')
print(q)

r = ['c', 'd', 'e']
s = ['f', 'g', 'h']
q.extend(r)
q.extendleft(s)
print(q)

print(q.pop())
print(q.popleft())

q.rotate(3)
print(q)

