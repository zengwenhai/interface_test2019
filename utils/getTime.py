import time


def get_time():
    foramt_time = '%Y-%m-%d-%H-%M-%S'
    nowtime = time.strftime(foramt_time, time.localtime())
    return nowtime