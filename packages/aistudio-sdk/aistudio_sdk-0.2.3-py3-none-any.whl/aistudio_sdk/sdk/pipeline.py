# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2024 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了产线任务提交、查询、停止功能

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2024/3/2
"""
import os
from pathlib import Path
from prettytable import PrettyTable
from aistudio_sdk import log, config
from aistudio_sdk.constant.err_code import ErrorEnum
from aistudio_sdk.constant.const import AUTH_DIR, AUTH_TOKEN_FILE, LOG_DIR, LOG_LEVEL_FILE
from aistudio_sdk.utils.util import zip_dir, err_resp
from aistudio_sdk.requests import pipeline as pp_request

__all__ = [
    "set_config",
    "create",
    "query",
    "stop",
]


def get_detail_url(pipeline_id):
    """拼接产线详情链接"""
    return f"{config.STUDIO_MODEL_API_URL_PREFIX_DEFAULT}/pipeline/{pipeline_id}/detail"


def tabled_log_info(detail_list):
    """
    表格化打印
    tabled_log_info([
        ["pipeline_id", "args.summit_name", "status", "get_detail_url(pipeline_id)", "create_ime"], 
        [], 
        ...
    ])
    """
    table = PrettyTable()
    table.field_names = ["pid", "name", "status", "url", "createTime"]
    for detail in detail_list:
        table.add_row(detail)
    log.info(table)


class Pipeline():
    """
    pipeline类
    """
    OBJECT_NAME = "pipeline"

    def set_config(self, args):
        """
        配置: token, log_level
        """
        log.debug(f'鉴权配置，参数: {args}')
        token = args.token
        if token:
            try:
                # create folder
                if not os.path.exists(AUTH_DIR):
                    Path(AUTH_DIR).mkdir(parents=True, exist_ok=True)
                # save in file
                with open(AUTH_TOKEN_FILE, 'w') as file:
                    file.write(token)
                log.info(f"[OK] Configuration saved to: {AUTH_TOKEN_FILE}")
            except Exception as e:
                log.error(f"[Error] Configuration faild: {e}")

        log_level = args.log
        if log_level:
            try:
                # create folder
                if not os.path.exists(LOG_DIR):
                    Path(LOG_DIR).mkdir(parents=True, exist_ok=True)
                # save in file
                with open(LOG_LEVEL_FILE, 'w') as file:
                    file.write(log_level)
                log.info(f"[OK] Configuration saved to: {LOG_LEVEL_FILE}")
            except Exception as e:
                log.error(f"[Error] Configuration faild: {e}")


    def get_auth(self):
        """
        获取鉴权token
        """
        if not os.path.exists(AUTH_TOKEN_FILE):
            return None
        try:
            with open(AUTH_TOKEN_FILE, 'r') as file:
                return file.read().strip()
        except Exception as e:
            log.error(f"[Error] Read configuration faild: {e}")
            return None
    

    def create(self, args):
        """
        创建产线任务
        """
        log.debug(f'创建产线，参数: {args}')

        # 校验
        token = self.get_auth()
        if not token:
            log.error(err_resp(
                ErrorEnum.TOKEN_IS_EMPTY.code, 
                ErrorEnum.TOKEN_IS_EMPTY.message + ', 请使用 aistudio config --token {yourToken}'
            ))
            return
        if len(args.mount_dataset) > config.MOUNT_DATASET_LIMIT:
            log.error(err_resp(
                ErrorEnum.PARAMS_INVALID.code, 
                f"{ErrorEnum.PARAMS_INVALID.message}: 单个任务最多挂载{config.MOUNT_DATASET_LIMIT}个数据集"
            ))
            return

        # 代码打包
        input_path = args.path
        zip_file = f"{input_path}.zip"
        if not os.path.exists(input_path):
            log.error(err_resp(
                ErrorEnum.FILE_NOT_FOUND.code, 
                ErrorEnum.FILE_NOT_FOUND.message
            ))
            return
        if not os.path.isdir(input_path):
            log.error(err_resp(
                ErrorEnum.NEED_FOLDER.code, 
                ErrorEnum.NEED_FOLDER.message
            ))
            return
        try:
            log.debug(f"step 1: 开始打包代码... {input_path}")
            zip_dir(input_path, zip_file)
            log.debug(f"代码打包完成! {zip_file}")
        except Exception as e:
            log.error(err_resp(
                ErrorEnum.INTERNAL_ERROR.code, 
                f"{ErrorEnum.INTERNAL_ERROR.message}: 压缩出错\n{e}"
            ))
            return
        if config.PIPELINE_CODE_SIZE_LIMIT < os.stat(zip_file).st_size:
            log.error(err_resp(
                ErrorEnum.FILE_TOO_LARGE.code, 
                f"{ErrorEnum.FILE_TOO_LARGE.message}: 代码包总体积不能超过 {config.PIPELINE_CODE_SIZE_LIMIT / 1024 / 1024} MB"
            ))
            return
        
        # 请求创建产线（仅参数校验）
        try:
            log.debug("step 2: 请求参数校验...")
            dataset_list = []
            for dataset_id in args.mount_dataset:
                dataset_list.append({
                    "datasetId": dataset_id
                })
            resp = pp_request.create(
                token, 
                args.summit_name, 
                args.cmd, 
                args.env, 
                args.device, 
                args.gpus,
                args.payment, 
                dataset_list
            )
        except pp_request.RequestPipelineException as e:
            log.error(err_resp(
                ErrorEnum.REQUEST_CREATE_PIPELINE_FAILED.code, 
                f"{ErrorEnum.REQUEST_CREATE_PIPELINE_FAILED.message}: {e[:500]}"
            ))
            return
        if resp["errorCode"] != ErrorEnum.SUCCESS.code:
            log.error(err_resp(
                ErrorEnum.REQUEST_CREATE_PIPELINE_FAILED.code, 
                f'{ErrorEnum.REQUEST_CREATE_PIPELINE_FAILED.message}: {resp["errorMsg"]}',
                resp["errorCode"],
                resp["logId"],
            ))
            return
        log.debug("参数校验成功!")
        pipeline_id = resp["result"]["pipelineId"]
        
        # 申请ak/sk
        try:
            log.debug("step 3: 请求申请ak/sk...")
            resp = pp_request.bosacl(token, pipeline_id)
        except pp_request.RequestPipelineException as e:
            log.error(err_resp(
                ErrorEnum.REQUEST_BOSACL_FAILED.code, 
                f"{ErrorEnum.REQUEST_BOSACL_FAILED.message}: {e[:500]}"
            ))
            return
        if resp["errorCode"] != ErrorEnum.SUCCESS.code:
            log.error(err_resp(
                ErrorEnum.REQUEST_BOSACL_FAILED.code, 
                f'{ErrorEnum.REQUEST_BOSACL_FAILED.message}: {resp["errorMsg"]}',
                resp["errorCode"],
                resp["logId"],
            ))
            return
        log.debug("申请ak/sk成功!")

        result = resp["result"]
        endpoint = result["endpoint"]
        bucket_name = result["bucketName"]
        file_key = result["fileKey"]
        access_key_id = result["accessKeyId"]
        secret_access_key = result["secretAccessKey"]
        session_token = result["sessionToken"]
        
        # bos上传
        try:
            log.debug("step 4: 代码上传bos...")
            pp_request.bos_upload(
                zip_file, 
                endpoint, 
                bucket_name, 
                file_key, 
                access_key_id, 
                secret_access_key, 
                session_token
            )
        except Exception as e:
            # 创建产线回调
            pp_request.create_callback(
                token, 
                pipeline_id, 
                False
            )
            log.error(err_resp(
                ErrorEnum.BOS_UPLOAD_FAILED.code, 
                f"{ErrorEnum.BOS_UPLOAD_FAILED.message}: {e[:500]}"
            ))
            return
        log.debug("代码上传成功!")
        
        # 创建产线回调
        try:
            log.debug("step 5: 回调请求创建产线...")
            resp = pp_request.create_callback(
                token, 
                pipeline_id, 
                True, 
                file_key, 
                os.path.basename(zip_file)
            )
        except pp_request.RequestPipelineException as e:
            log.error(err_resp(
                ErrorEnum.REQUEST_CREATE_PIPELINE_CALLBACK_FAILED.code, 
                f"{ErrorEnum.REQUEST_CREATE_PIPELINE_CALLBACK_FAILED.message}: {e[:500]}"
            ))
            return
        if resp["errorCode"] != ErrorEnum.SUCCESS.code:
            log.error(err_resp(
                ErrorEnum.REQUEST_CREATE_PIPELINE_CALLBACK_FAILED.code, 
                f'{ErrorEnum.REQUEST_CREATE_PIPELINE_CALLBACK_FAILED.message}: {resp["errorMsg"]}',
                resp["errorCode"],
                resp["logId"],
            ))
            return
        log.debug("创建成功!")
        
        result = resp["result"]
        stage = result["stage"]
        create_ime = result["createTime"]
        tabled_log_info([
            [
                pipeline_id, 
                args.summit_name, 
                stage, 
                get_detail_url(pipeline_id), 
                create_ime
            ]
        ])


    def query(self, args):
        """
        查询产线
        """
        log.debug(f'查询产线，参数: {args}')

        # 校验
        token = self.get_auth()
        if not token:
            log.error(err_resp(
                ErrorEnum.TOKEN_IS_EMPTY.code, 
                ErrorEnum.TOKEN_IS_EMPTY.message + ', 请使用 aistudio config --token {yourToken}'
            ))
            return
        
        # 请求
        try:
            resp = pp_request.query(
                token, 
                args.query_pipeline_id, 
                args.name, 
                args.status
            )
        except pp_request.RequestPipelineException as e:
            log.error(err_resp(
                ErrorEnum.REQUEST_QUERY_PIPELINE_FAILED.code, 
                f"{ErrorEnum.REQUEST_QUERY_PIPELINE_FAILED.message}: {e[:500]}"
            ))
            return
        if resp["errorCode"] != ErrorEnum.SUCCESS.code:
            log.error(err_resp(
                ErrorEnum.REQUEST_QUERY_PIPELINE_FAILED.code, 
                f'{ErrorEnum.REQUEST_QUERY_PIPELINE_FAILED.message}: {resp["errorMsg"]}',
                resp["errorCode"],
                resp["logId"],
            ))
            return
        
        data = list()
        for res in resp["result"]:
            data.append(
                [
                    res["pipelineId"], 
                    res["pipelineName"], 
                    res["stage"], 
                    get_detail_url(res["pipelineId"]), 
                    res["createTime"]
                ]
            )
        tabled_log_info(data)

    def stop(self, args):
        """
        停止产线
        """
        log.debug(f'停止产线，参数: {args}')

        # 校验
        token = self.get_auth()
        if not token:
            log.error(err_resp(
                ErrorEnum.TOKEN_IS_EMPTY.code, 
                ErrorEnum.TOKEN_IS_EMPTY.message + ', 请使用 aistudio config --token {yourToken}'
            ))
            return
        
        # 请求
        try:
            resp = pp_request.stop(token, args.stop_pipeline_id)
        except pp_request.RequestPipelineException as e:
            log.error(err_resp(
                ErrorEnum.REQUEST_STOP_PIPELINE_FAILED.code, 
                f"{ErrorEnum.REQUEST_STOP_PIPELINE_FAILED.message}: {e[:500]}"
            ))
            return
        if resp["errorCode"] != ErrorEnum.SUCCESS.code:
            log.error(err_resp(
                ErrorEnum.REQUEST_STOP_PIPELINE_FAILED.code, 
                f'{ErrorEnum.REQUEST_STOP_PIPELINE_FAILED.message}: {resp["errorMsg"]}',
                resp["errorCode"],
                resp["logId"],
            ))
            return
        log.info('[OK] 停止成功.')
    

def set_config(*args):
    """config"""
    return Pipeline().set_config(*args)

def create(*args):
    """create"""
    return Pipeline().create(*args)

def query(*args):
    """query"""
    return Pipeline().query(*args)

def stop(*args):
    """stop"""
    return Pipeline().stop(*args)
