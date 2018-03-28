# !/usr/bin/env python
# coding=utf-8

from atexit import register
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen
from re import compile

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# TODO 排名数据为异步获取，字段取不到，查找相关资料

DANGURL = 'http://product.dangdang.com/index.php?r=callback/get-bang-rank&productId={0}'

REGEX = compile(r"\\")

ISBNs = {
    '23473514': u'Python 基础教程',
    '23961748': u'Python 核心编程（第三版）',
    '21063086': u'Python 学习手册'
}


def _getRanking(isbn):
    bookDict = {}
    # TODO 参数可用 str.format() 方法： '{0}{1}'.format(*args)
    ajax = uopen(DANGURL.format(isbn))
    rank = eval(ajax.read())["data"]
    type_name = rank['pathName'].decode('unicode-escape')
    bookDict['type'] = REGEX.sub('', type_name)
    bookDict['rank'] = rank['rank']
    ajax.close()
    return bookDict
    # return REGEX.findall('\d+', str(span))[0]

# def _getRanking2(isbn):
#     bookDict = {}
#     with uopen(DANGURL.format(isbn)) as page:
#         print page
#         # rank = eval(page.read())["data"]
#         # print rank
#         # type_name = rank['pathName'].decode('unicode-escape')
#         # bookDict['type'] = REGEX.sub('', type_name)
#         # bookDict['rank'] = rank['rank']
#         # return bookDict

def _showRanking(isbn):
    dictObj = _getRanking(isbn)
    print '- %s 在 %s 中排名：%s' % (ISBNs[isbn], dictObj["type"], dictObj["rank"])


def _main():
    print 'At', ctime(), 'on dangdang...'
    for isbn in ISBNs:
        Thread(target=_showRanking, args=(isbn,)).start()

@register
def _atexit():
    print 'all DONE at:', ctime()

if __name__ == '__main__':
    _main()
