# !/usr/bin/env python
# coding=utf-8

"""代码用于下载 Web 页面，显示页面的第一行 & 最后一行"""

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webPage):
    f = open(webPage)
    lines = f.readlines()
    f.close()
    # for eachLine in lines:
    #     if not eachLine.strip():
    #         continue
    #     else:
    #         print eachLine,
    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)

def download(url="http://www.taobao.com", process=firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None

    if retval:
        process(retval)

if __name__ == "__main__":
    download()