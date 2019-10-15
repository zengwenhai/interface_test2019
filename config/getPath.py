import os


def getpath(filepath, filename):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath, filename)


if __name__ == "__main__":
    print(getpath('config', 'config.ini'))
    #print(getpath(dirname='data', filepath='report', filename='TestReport2019-10-10-13-53-31.html'))