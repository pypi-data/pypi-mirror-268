# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  qlvClient
# FileName:     utils.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/17
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import re
import hashlib
import logging
from datetime import datetime, timedelta

logger = logging.getLogger("root")

standard_date_format = "%Y-%m-%d %H:%M:%S"


def iso_to_standard_datestr(datestr: str, time_zone_step: int) -> str:
    """iso(2024-04-21T04:20:00Z)格式转 标准的时间格式(2024-01-01 00:00:00)"""
    dt_str = "{} {}".format(datestr[:10], datestr[11:-1])
    dt = datetime.strptime(dt_str, standard_date_format)
    dt_step = dt + timedelta(hours=time_zone_step)
    return dt_step.strftime(standard_date_format)


def current_datetime_str() -> str:
    return datetime.now().strftime(standard_date_format)


def encryp_md5(data: str) -> str:
    # 创建一个 hashlib.md5 对象
    md5_hash = hashlib.md5()
    # 将输入的字符串转换为 bytes，并更新 MD5 哈希对象
    md5_hash.update(data.encode())
    # 获取 MD5 值的十六进制表示形式（32 位小写）
    md5_hex_digest = md5_hash.hexdigest()
    return md5_hex_digest


def covert_dict_key_to_lower(d: dict) -> dict:
    result = dict()
    for key, value in d.items():
        if isinstance(key, str):
            key_new = key.lower()
            result[key_new] = value
    return result


def get_html_title(html: str) -> str:
    # 使用正则表达式提取目标字符串
    pattern = '<title>(.*?)</title>'
    match = re.search(pattern, html)
    if match:
        title = match.group(1)
    else:
        title = "Abnormal HTML document structure"
    return title
