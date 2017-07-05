# coding=utf-8
try:
    fileName = raw_input('请输入文件名：')
    fobj = open(fileName, 'r')
    for eachLine in fobj:
        print eachLine,

    fobj.close()
except IOError, e:
    print '文件打开时出错', e