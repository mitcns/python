# !/usr/bin/env/ python
# coding=utf-8

"""整型素数因子"""


def isPrime(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            return False
        count -= 1
    else:
        return True


def primeFactors(num):
    if isPrime(num):
        yield 1
        yield num
    else:
        count = num / 2
        prime = 2
        while prime <= count:
            if num % prime == 0:
                yield prime
                num /= prime
            else:
                prime += 1


if __name__ == "__main__":
    num = int(raw_input("请输入要转换的整数："))
    print "%d的素因子是" % num,
    for item in primeFactors(num):
        print item,
