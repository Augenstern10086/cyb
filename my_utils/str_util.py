# -*- coding:UTF-8 -*-
"""
editor:ChangYingbo
date:2024年 09月 11日
"""
def str_reverse(s):
    """
    功能是将字符串完成反转
    :param s:将被反转的字符串
    :return:反转后的字符串
    """
    l = s[::-1]
    return l

def substr(s, x, y):
    l = s[x:y:1]
    return l

if __name__ == "__main__":
    s = str_reverse("1234")
    s1 = substr("1234",1,2)
    print(s)
    print(s1)