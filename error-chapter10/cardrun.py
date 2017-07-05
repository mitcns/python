# !/usr/bin/env python
# coding=utf-8

"""信用卡交易系统"""

def safeFloat(obj):
    "safe version of float"
    try:
        retval = float(obj)
    except (ValueError, TypeError), e:
        retval = str(e)
    return retval

def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
        txns = ccfile.readlines()
    except IOError, e:
        log.write('no txns this month\n')
        log.close()
    finally:
        ccfile.close()

    total = 0.00
    log.write('account log:\n')

    for eachTxn in txns:
        result = safeFloat(eachTxn)
        if isinstance(result, float):
            total += result
            log.write('data... processed\n')
        else:
            log.write('ignored: %s' % result)

    print '$ %.2f (new balance)' % total
    log.write('total money is %.2f' % total)
    log.close()

if __name__ == "__main__":
    main()