import string
from collections import namedtuple

def str_count(s):
    count_en = count_dg = count_sp = count_zh = count_oth = 0

    for c in s:
        # 英文
        if c in string.ascii_letters:
            count_en += 1
        # 数字
        elif c.isdigit():
            count_dg += 1
        # 空格
        elif c.isspace():
            count_sp += 1
        # 中文
        elif c.isalpha():
            count_zh += 1
        # 特殊字符
        else:
            count_oth += 1

    print ("英文=%d，数字=%d，空格=%d，中文=%d，特殊字符=%d" % (count_en,count_dg,count_sp,count_zh,count_oth))
