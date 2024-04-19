#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    tools
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2024/4/17    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import hashlib, json, math
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

