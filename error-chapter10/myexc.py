# !/usr/bin/env python
# coding=utf-8

"""自定义新异常 FileError 和 NetworkError"""

import os, socket, errno, types, tempfile

class NetworkError(IOError):
    pass

class FileError(IOError):
    pass

def updArgs(args, newArg=None):
    if isinstance(args, IOError):
        myArgs = []
        myArgs.extend([arg for arg in args])
    else:
        myArgs = list(args)

    if newArg:
        myArgs.append(newArg)

    return tuple(myArgs)

def fileArgs(fileName, mode, args):
    if args[0] == errno.EACCES and 'access' in dir(os):
        perms = ''
        permd = {
            'r': os.R_OK,
            'w': os.W_OK,
            'x': os.X_OK
        }
        pkeys = permd.keys()
        pkeys.sort()
        # pkeys.reverse()

        for eachPerm in pkeys:
            if os.access(fileName, permd[eachPerm]):
                perms += eachPerm
            else:
                perms += '-'

        if isinstance(args, IOError):
            myArgs = []
            myArgs.extend([arg for arg in args])
        else:
            myArgs = list(args)

        myArgs[1] = "'%s' %s (perms: '%s')" % (mode, myArgs[1], perms)
        myArgs.append(args.filename)

    else:
        myArgs = args

    return tuple(myArgs)

def myConnect(sock, host, port):
    try:
        sock.connect((host, port))

    except socket.error, args:
        myArgs = updArgs(args)
        if len(myArgs) == 1:
            myArgs = (errno.ENXIO, myArgs[0])

        raise NetworkError, updArgs(myArgs, host + ': ' + str(port))

def myOpen(fileName, mode='r'):
    try:
        fo = open(fileName, mode)
    except IOError, args:
        raise FileError, fileArgs(fileName, mode, args)

    return fo

def testFile():
    fileObj = tempfile.mktemp()
    f = open(fileObj, 'w')
    f.close()

    for eachTest in ((0, 'r'), (0100, 'r'), (0400, 'w'), (0500, 'w')):
        try:
            os.chmod(fileObj, eachTest[0])
            f = myOpen(fileObj, eachTest[1])
        except FileError, args:
            print "%s: %s" % (args.__class__.__name__, args)
        else:
            print fileObj, "opend ok... perm ignored"
            f.close()
    os.chmod(fileObj, 0777)
    os.unlink(fileObj)

def testNet():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for eachHost in ('127.0.0.1', 'www'):
        try:
            myConnect(s, eachHost, 8080)
        except NetworkError, args:
            print "%s: %s" % (args.__class__.__name__, args)

if __name__ == "__main__":
    testFile()
    testNet()