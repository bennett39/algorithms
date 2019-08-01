import os

root = os.path.expanduser('~/')
l = os.listdir(root)
for f in l:
    path = os.path.join(root, f)
    if os.path.isdir(path):
        print(f)
