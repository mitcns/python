# !/usr/bin/env python
# coding=utf-8

"""   *** 动态生成和执行 Python 代码 ***
    简单、迅速生成和执行循环的计算机辅助软件工程。
"""
dashes = '\n' + '-' * 50  # dashed line
execDict = {
    'f': """  # for loop
for %s in %s:
    print %s
""",
    's': """  # sequence while loop
%s = 0
%s = %s
while %s < len(%s):
    print %s[%s]
    %s = %s + 1
""",
    'n': """  # counting while loop
%s = %d
while %s < %d:
    print %s
    %s = %s + %d
"""
}

def main():

    ltype = raw_input('Loop type? (For/While) ').lower()
    dtype = raw_input('Data type? (Number/Seq) ').lower()

    if dtype == 'n':
        start = input('Starting value?')
        stop = input('Ending value (non-inclusive)?')
        step = input('Stepping value?')
        seq = str(range(start, stop, step))
    else:
        seq = raw_input('Enter sequence:')

    var = raw_input('Iterative variable name?')

    if ltype == 'f':
        execStr = execDict['f'] % (var, seq, var)
    elif ltype == 'w':
        if dtype == 's':
            svar = raw_input('Enter sequence name?')
            execStr = execDict['s'] % (var, svar, var, stop, var,  var, var, step)
        elif dtype == 'n':
            execStr = execDict['n'] % (var, start, var, stop, var, var, var, step)
    print dashes
    print 'Your custom-generated code:' + dashes
    print execStr + dashes
    print 'Test execution of the code:' + dashes
    exec execStr
    print dashes


if __name__ == '__main__':
    main()
