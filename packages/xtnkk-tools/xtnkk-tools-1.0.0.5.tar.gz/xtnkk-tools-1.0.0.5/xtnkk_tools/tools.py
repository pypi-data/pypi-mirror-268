#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    tools
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2024/4/17    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import hashlib, time


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


def get_now_time_int(is_time_10=False, is_time_13=False):
    """
        获取当前时间戳
    :param is_time_10: 是否需要处理为10位的时间戳，默认不处理
    :param is_time_13: 是否需要处理为13位的时间戳，默认不处理
    :return:
    """
    if is_time_10:
        return int(time.time())
    elif is_time_13:
        return int(time.time() * 1000)
    return time.time()


if __name__ == '__main__':
    print(get_md5_16("1", True))  # 获取16位md5结果
    print(get_md5_32("1", True))  # 获取32位md5结果
    print(get_now_time_int())  # 获取当前时间戳
    print(get_now_time_int(True, False))  # 获取当前10位时间戳
    print(get_now_time_int(False, True))  # 获取当前13位时间戳
