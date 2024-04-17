# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了常用的工具函数

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2023/07/24
"""
import os
import re
import base64
import hashlib
from datetime import datetime
import zipfile


class Dict(dict):
    """dict class"""
    def __getattr__(self, key):
        value = self.get(key, None)
        return Dict(value) if isinstance(value, dict) else value
    
    def __setattr__(self, key, value):
        self[key] = value


def convert_to_dict_object(resp):
    """
    Params
        :resp: dict, response from AIStudio
    Rerurns
        AIStudio object
    """
    if isinstance(resp, dict):
        return Dict(resp)
    
    return resp


def err_resp(sdk_code, msg, biz_code=None, log_id=None):
    """
    Params
        :error_code: sdk错误码
        :msg: 错误信息
        :biz_code: 上游接口错误码透传
        :log_id: 上游接口错误日志id透传
    Rerurns
        formatted error msg
    """
    return {
        "error_code": sdk_code,
        "error_msg": msg,
        "biz_code": biz_code,
        "log_id": log_id
    }


def is_valid_host(host):
    """检测host合法性"""
    # 去除可能的协议前缀 如http://、https://
    host = re.sub(r'^https?://', '', host, flags=re.IGNORECASE)
    result = is_valid_domain(host)
    # if not result:
    #     host = re.sub(r'^http?://', '', host, flags=re.IGNORECASE)
    #     result = is_valid_domain(host)
    return result


def is_valid_domain(domain):
    """检测域名合法性"""
    return True
    # pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$"
    # return re.match(pattern, domain) is not None


def calculate_sha256(file_path):
    """将文件计算为sha256值"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # 逐块更新哈希值，以适应大型文件
        while True:
            data = file.read(65536)  # 64K块大小
            if not data:
                break
            sha256_hash.update(data)

    return sha256_hash.hexdigest()


def gen_ISO_format_datestr():
    """
    # 生成 ISO 8601日期时间格式
    # 例如"2023-09-12T11:29:45.703Z"
    """
    # 获取当前日期和时间
    now = datetime.now()
    # 使用strftime函数将日期和时间格式化为所需的字符串格式
    formatted_date = now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return formatted_date


def gen_MD5(file_path):
    """将文件计算为md5值"""
    md5_hash = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            # 逐块读取文件并更新哈希对象
            while True:
                data = file.read(4096)  # 读取4K字节数据块
                if not data:
                    break
                md5_hash.update(data)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None

    # 获取MD5哈希值的十六进制表示
    md5_hex = md5_hash.hexdigest()

    return md5_hex


def gen_base64(original_string):
    """将字符串计算为base64"""
    # 将原始字符串编码为字节数组
    bytes_data = original_string.encode('utf-8')
    # 使用base64进行编码
    base64_encoded = base64.b64encode(bytes_data).decode('utf-8')
    return base64_encoded


def create_sha256_file_and_encode_base64(sha256, size):
    """生成指定内容的文件并进行base64编码字符串返回"""
    content = f"version https://git-lfs.github.com/spec/v1\noid sha256:{sha256}\nsize {size}"
    name = 'sha256_value'
    with open(name, 'w') as file:
        file.write(content)

    ret = file_to_base64(name)
    os.remove(name)
    return ret


def file_to_base64(filename):
    """读取文件内容并进行Base64编码"""
    with open(filename, "rb") as file:
        contents = file.read()
        encoded_contents = base64.b64encode(contents)
    return encoded_contents.decode('utf-8')


def zip_dir(dirpath, out_full_name):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param out_full_name: 压缩文件保存路径 xxxx.zip
    :return: 无
    """
    zip_obj = zipfile.ZipFile(out_full_name, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip_obj.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip_obj.close()
