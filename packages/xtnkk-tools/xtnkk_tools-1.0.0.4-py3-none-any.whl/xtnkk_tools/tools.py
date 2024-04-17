#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    tools
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2024/4/17    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import hashlib


def get_md5_32(s, is_upper=False):
    """
        获取文本的md5值 32位
    :param s: 文本
    :param is_upper: 是否转大写 默认False
    :return:
    """
    # s.encode()#变成bytes类型才能加密
    m = hashlib.md5(s.encode())  # 长度是32
    if is_upper:
        return m.hexdigest().upper()
    return m.hexdigest()


def get_md5_16(s, is_upper=False):
    """
        获取文本的md5值 16位
    :param s: 文本
    :param is_upper: 是否转大写 默认False
    :return:
    """
    result = get_md5_32(s, is_upper)
    return result[8:24]


if __name__ == '__main__':
    print(get_md5_16("1", True))
    print(get_md5_32("1", True))
