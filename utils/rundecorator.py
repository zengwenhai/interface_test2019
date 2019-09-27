from functools import wraps

# def deco(a):
#     def decorator_name(f):
#         @wraps(f)
#         def inner(*args, **kwargs):
#             if a == 'yes':
#                f(*args, **kwargs)
#         return inner
#     return decorator_name
#
#
# @deco('yes')
# def a():
#     print("123")
#
#
# a()


def run_test(flag=None):
    def outer(func):  # 1第一步
        @wraps(func)  # 3第三步
        def inner(*args, **kwargs):
            if flag == 'yes':
                print("====start====")  # 5第五步
                f = func(*args, **kwargs)  # 6第六步
                print("====finally====")  # 7第七步
            else:
                print("不执行该函数")
            # return f
        return inner  # 4第四步
    return outer

"""
装饰器功能：
    1.自动执行outer函数并且将它下面的函数名f1当做参数传递
    2.将outer函数的返回值，重新赋值给f1(一个函数被装饰器装饰了，就会被重新赋值为装饰器的内层函数)
    3.再次执行f1函数时，将不会执行原函数f1，而是执行outer函数返回赋值给f1的inner函数
"""


@run_test(flag='yes')  # 2第二步
def f1(a):
    print("input:%s" % a)
    return "pass"