import os


def walk(dirname, level=0):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print('| %s %s' % (' - '*level, name))
        else:
            walk(path, level + 1)


walk(os.getcwd())
