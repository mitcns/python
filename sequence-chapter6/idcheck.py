# coding=utf-8
# !/usr/bin/env python
# 导入 string 模块

'''标识符检查'''
import string

alphas = string.letters + "_"
nums = string.digits
alphaNums = alphas + nums

print '''Welcome to the Identifier Chacker v1.0
欢迎使用标识符检查器-1.0'''
print '''Testees must be at least 2 chars long.
标识符长度至少为两位'''

inp = raw_input('请输入标识符：')
inpLen = len(inp)
remainTest = 'Python'


def identifier(inp):
    if inpLen > 1:
        if inp[0] not in alphas:
            print '''invalid: first symbol must be alphabetic
            无效：首字符必须为字母或者下划线！'''
        else:
            sequeObj = inp[1:]
            for otherChar in sequeObj:
                if otherChar not in alphaNums:
                    print '''invalid: remaining symbols must be alphanumeric
                    无效：输入的标识符需为字母、数字或者下划线！'''
                    break
            else:
                if inp == remainTest:
                    print '输入值为Python关键字'
                    return
                print """okay as an identifier
                该输入可作用标识符"""

    elif inpLen == 1:
        print "您输入的字符长度为一！"
        #identifier(inp)


if __name__ == '__main__':
    identifier(inp)
