#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    tools
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2024/4/17    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import hashlib, time, datetime, json, math
from urllib.parse import urlencode


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


def get_file_md5_32(file_path):
    """
        获取文件md5值
    :param file_path: 文件路径
    :return: 
    """
    with open(file_path, 'rb') as file:
        data = file.read()
        md5_hash = hashlib.md5(data).hexdigest()
    return md5_hash


def get_file_md5_16(file_path):
    """
        获取文件md5值
    :param file_path: 文件路径
    :return: 
    """
    result = get_file_md5_32(file_path)
    return result[8:24]


def get_now_time_int(is_time_10=False, is_time_13=False, is_time_day0=False, is_time_day59=False):
    """
        获取当前时间戳
    :param is_time_10: 是否需要处理为10位的时间戳，默认不处理
    :param is_time_13: 是否需要处理为13位的时间戳，默认不处理
    :param is_time_day0: 是否需要处理为当天00:00:00点时间戳，默认不处理
    :param is_time_day59: 是否需要处理为当天23:59:59点时间戳，默认不处理
    :return:
    """

    if is_time_10:
        val = int(time.time())
    elif is_time_13:
        val = int(time.time() * 1000)
    else:
        val = time.time()
    if is_time_day0:
        val = get_now_day0_time_int(is_time_13)
    elif is_time_day59:
        val = get_now_day59_time_int(is_time_13)
    return val


def get_now_day0_time_int(is_time_13=False):
    """
        获取当天0点时间戳
    :param is_time_13: 是否需要处理为13位的时间戳，默认不处理并且返回10位时间戳
    :return:
    """
    val = time.mktime(datetime.date.today().timetuple())
    if is_time_13:
        return int(val * 1000)
    else:
        return int(val)


def get_now_day59_time_int(is_time_13=False):
    """
        获取当天23:59:59点时间戳
    :param is_time_13: 是否需要处理为13位的时间戳，默认不处理并且返回10位时间戳
    :return:
    """
    # 获取当前日期时间
    now = datetime.datetime.now()
    # 设置小时、分钟、秒为 23:59:59
    last_second = now.replace(hour=23, minute=59, second=59)
    # 转换为时间戳
    timestamp = time.mktime(last_second.timetuple())
    # 转换为整数类型
    if is_time_13:
        return int(timestamp * 1000)
    else:
        return int(timestamp)


def get_str_to_json(str_json):
    """
        字符串类型的json格式 转 json
    :param str_json: 字符串json
    :return:
    """
    try:
        new_str_json = str_json.replace("'", '"'). \
            replace("None", "null").replace("True", "true"). \
            replace("False", "false")
        return json.loads(new_str_json)
    except Exception as e:
        return {}


def get_build_url_with_params(url, params):
    """
        传入url和params拼接完整的url ->效果 https://wwww.xxxx.com/?xxx1=1&xxx2=2
    :param url:
    :param params:
    :return:
    """
    encoded_params = urlencode(params)
    full_url = url + "?" + encoded_params
    return full_url


def get_calculate_total_page(total, limit):
    """
        根据total和limit计算出一共有多少页
    :param total:
    :param limit:
    :return:
    """
    if limit <= 0:
        return 0
    # 根据总条数和limit计算总页数
    total_pages = math.ceil(total / limit)
    return total_pages


if __name__ == '__main__':
    pass
    # print(get_md5_16("1", True))  # 获取16位md5结果
    # print(get_md5_32("1", True))  # 获取32位md5结果
    # print(get_now_time_int())  # 获取当前时间戳
    # print(get_now_time_int(True, False))  # 获取当前10位时间戳
    # print(get_now_time_int(False, True))  # 获取当前13位时间戳
    # print(get_now_time_int(True, False, True, False))  # 获取当天0点10位时间戳
    # print(get_now_time_int(False, True, True, False))  # 获取当天0点13位时间戳
    # print(get_now_time_int(True, False, False, True))  # 获取当天23:59:59 10位时间戳
    # print(get_now_time_int(False, True, False, True))  # 获取当天23:59:59 13位时间戳
    # print("获取当天0点时间戳", get_now_day0_time_int(False))  # 获取当天0点时间戳
    # print("获取当天0点时间戳", get_now_day0_time_int(True))  # 获取当天0点时间戳
    # print("获取当天23:59:59点时间戳", get_now_day59_time_int(False))  # 获取当天23:59:59点时间戳
    # print("获取当天23:59:59点时间戳", get_now_day59_time_int(True))  # 获取当天23:59:59点时间戳
