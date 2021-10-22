import os

root = 'C:/Root'

for song in os.listdir(root):
    for file in os.listdir(os.path.join(root,song)):
        print(file)
    print('\n')