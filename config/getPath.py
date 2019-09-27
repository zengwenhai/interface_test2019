import os


def getpath(filepath, filename):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath, filename)


if __name__ == "__main__":
    print(getpath('config', 'config.ini'))