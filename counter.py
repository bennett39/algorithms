import collections

c = collections.Counter('oasis')
print(c.most_common())
print(sorted(c))
print(''.join(sorted(c.elements())))
print(sum(c.values()))
print(len(c))

for letter in 'qwerty':
    c[letter] += 1

print(c)
d = collections.Counter('zookeeper')
c.update(d)
print(c)
c.clear()
print(c)
