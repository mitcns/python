# !/usr/bin/env python
# coding=utf-8

"""safe raw_input func"""

def raw_input_safe(tip):
    try:
        inputStr = raw_input(tip)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return inputStr

if __name__ == "__main__":
    print raw_input_safe("请任性输入：")