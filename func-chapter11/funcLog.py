# !/usr/bin/env python
# coding=utf-8

"""用户选择在函数调用之前或之后，吧函数调用写入日志"""

from time import time

def logged(when):
    def log(f, *args, **kArgs):
        print '''Called:
        function: %s
        args: %r
        kArgs: %r''' % (f, args, kArgs)

    def preLogged(f):
        def wrapper(*args, **kArgs):
            log(f, *args, **kArgs)
            return f(*args, **kArgs)
        return wrapper

    def postLogged(f):
        def wrapped(*args, **kArgs):
            now = time()
            try:
                return f(*args, **kArgs)
            finally:
                log(f, *args, **kArgs)
                print 'time delta: %s' % (time() - now)
        return wrapped

    try:
        return {
            'pre': preLogged,
            'post': postLogged
        }[when]
    except KeyError, e:
        raise ValueError(e), 'must be "pre" or "post"'
'装饰器还是很有用的！'
@logged("post")
def hello(*name):
    print 'Hello,', name

if __name__ == "__main__":
    hello('World!')
