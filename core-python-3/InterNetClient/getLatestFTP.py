# !/usr/bin/env python
# coding=utf-8

import os, socket
from ftplib import FTP, error_perm
# from httplib import HTTPS, error TODO mozilla 已经改为 HTTPS 文件传输，查阅相关资料后完善脚本

HOST = 'ftp.mozilla.org'
DIRN = 'pub/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def ftpMain():

    try:
        f = FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'ERROR: cannot reach "%s"' % HOST
        return
    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymously"'

    try:
        f.cwd(DIRN)
    except error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
        f.quit()

if __name__ == '__main__':
    ftpMain()
