# !/usr/bin/env python
# coding=utf-8

import os
for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print "temp 文件路径不可用"
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print "*** 当前临时文件目录："
    print cwd

    print "*** 创建一个示例文件目录"
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()

    print "*** 新的工作目录:"
    print cwd
    print "*** 初始目录文件列表："
    print os.listdir(cwd)

    print "*** 创建测试文件"
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print "*** 更新目录列表"
    print os.listdir(cwd)

    print "*** 将 'test'文件重命名为 'filetest.txt'"
    os.rename('test', 'filetest.txt')
    print "*** 更新目录列表"
    print os.listdir(cwd)

    path = os.path.join(cwd, os.listdir(cwd)[0])
    print "*** 所有文件 路径名"
    print path
    print "*** (pathname, basename) =="
    print os.path.split(path)
    print "*** (filename, extension) =="
    print os.path.splitext(os.path.basename(path))

    print "*** 展示文件内容："
    fobj = open(path)
    for eachLine in fobj:
        print eachLine
    fobj.close()

    print "*** 删除text文件"
    os.remove(path)
    print "*** 更新目录列表"
    print os.listdir(cwd)
    os.chdir(os.pardir)
    print "*** 删除test目录"
    os.rmdir('example')
    print "*** DONE"