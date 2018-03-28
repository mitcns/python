# !/usr/bin/env python
# coding=utf-8

"""some func for test sys performance"""

def testIt(func, *nkwArgs, **kwargs):
    try:
        retval = func(*nkwArgs, **kwargs)
        result = (True, retval)
    except Exception, e:
        result = (False, str(e))
    return result

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234', '12.34')

    for eachFunc in funcs:
        print '-_' * 20
        for eachVal in vals:
            retval = testIt(eachFunc, eachVal)
            if retval[0]:
                print '%s(%s)= ' % (eachFunc.__name__, eachVal), retval[1]
            else:
                print '%s(%s)= FAILED:' % (eachFunc.__name__, eachVal), retval[1]


if __name__ == "__main__":
    test()