import os

d = os.listdir(os.path.abspath(os.curdir))
print(d)
res = {}

for fi in d:
    res[fi] = []
    if os.path.isfile(fi):
        with open(fi, mode='r', errors='ignore') as f:
            for line in f:
                res[fi].append(line.strip())

with open('output.txt', mode='w', errors='ignore') as g:
    for line in res:
        g.write(line)
