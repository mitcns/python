# !/usr/bin/env python
# coding=utf-8

# 获取用户输入
num_str = raw_input("Enter a number: ")

# 将用户输入转化为 int 类型
num_num = int(num_str)

# 创建一个1~用户输入数字的列表
fac_list = range(1, num_num + 1)
print "BEFORE:", fac_list

# 定义一个值为 0 的整型变量
i = 0
fac_reduce = []
# while 循环
while i < len(fac_list):

    # 用户输入取余
    if num_num % fac_list[i] != 0:
        fac_reduce.append(fac_list[i])
    # 变量自增
    i += 1

# 打印循环后的数值
print "AFTER:", fac_reduce
