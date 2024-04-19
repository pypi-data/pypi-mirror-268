#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2024 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
命令行

Authors: xiangyiqing(xiangyiqing@baidu.com)
Date:    2024/03/05
"""
import sys
import argparse
import click
from aistudio_sdk import log
from aistudio_sdk.sdk import pipeline

__all__ = [
    'main',
]


def init():
    """
    构建CLI Parser
    """
    parser = argparse.ArgumentParser(prog='PROG')
    subparser_aistudio = parser.add_subparsers(
        help='AI Studio CLI SDK'
    )

    # config
    config = subparser_aistudio.add_parser(
        'config', 
        help='首次使用AI Studio CLI管理任务时, 需要先使用AI Studio账号的访问令牌进行身份认证。\
            一次认证后，再次使用时无需认证。'
    )
    config.add_argument(
        '-t', '--token', 
        type=str, 
        required=False,
        default='',
        help='AI Studio账号的访问令牌'
    )
    config.add_argument(
        '-l', '--log', 
        type=str, 
        required=False,
        default='',
        choices=['info', 'debug', ''],
        help='日志级别'
    )

    # 提交
    submit = subparser_aistudio.add_parser(
        'submit', 
        help='提交SDK产线任务'
    )
    subparser_submit = submit.add_subparsers()
    submit_job = subparser_submit.add_parser(
        'job',
        help='提交SDK产线任务'
    )
    submit_job.add_argument(
        '-n', '--name', 
        type=str, 
        required=True,
        dest='summit_name',
        help='产线任务名称'
    )
    submit_job.add_argument(
        '-p', '--path', 
        type=str, 
        required=True, 
        help='代码包本地路径(文件夹)，要求文件总体积不超过50MB'
    )
    submit_job.add_argument(
        '-c', '--cmd', 
        type=str, 
        required=True,
        help='任务启动命令'
    )
    submit_job.add_argument(
        '-e', '--env', 
        type=str, 
        required=False, 
        default='paddle2.6_py3.10',
        choices=['paddle2.4_py3.7', 'paddle2.5_py3.10', 'paddle2.6_py3.10'],
        help='飞桨框架版本, 默认paddle2.6_py3.10'
    )
    submit_job.add_argument(
        '-d', '--device', 
        type=str, 
        required=False, 
        default='v100',
        choices=['v100'],
        help='硬件资源, 默认v100'
    )
    submit_job.add_argument(
        '-g', '--gpus', 
        type=int, 
        required=False, 
        default='1',
        choices=[1, 4, 8],
        help='gpu数量, 默认单卡'
    )
    submit_job.add_argument(
        '-pay', '--payment', 
        type=str, 
        required=False, 
        default='acoin',
        choices=['acoin', 'coupon'],
        help='计费方式: * acoin-A币 * coupon-算力点. 默认使用A币'
    )
    submit_job.add_argument(
        '-m', '--mount_dataset',
        action='append',
        type=int, 
        required=False,
        default=[],
        help='数据集挂载, 单个任务最多挂载3个'
    )

    # 查询
    jobs = subparser_aistudio.add_parser(
        'jobs', 
        help='查询SDK产线任务'
    )
    jobs.add_argument(
        'query_pipeline_id',
        type=str,
        nargs='?',
        default='',
        help='产线id'
    )
    jobs.add_argument(
        '-n', '--name',
        type=str,
        required=False,
        default='',
        help='产线名称'
    )
    jobs.add_argument(
        '-s', '--status',
        type=str,
        required=False,
        default='',
        help='状态'
    )

    # 停止
    stop = subparser_aistudio.add_parser(
        'stop', 
        help='停止SDK产线任务'
    )
    subparser_stop = stop.add_subparsers()
    stop_job = subparser_stop.add_parser(
        'job', 
        help='停止SDK产线任务'
    )
    stop_job.add_argument(
        'stop_pipeline_id',
        type=str,
        help='产线id'
    )
    stop_job.add_argument(
        '-f', '--force', 
        action='store_true',
        help='强制停止，无需二次确认'
    )

    return parser


def main():
    """CLI入口"""
    parser = init()
    args = sys.argv[1:]
    try:
        args = parser.parse_args(args)
    except:
        return
    
    if "token" in args:
        pipeline.set_config(args)
    elif "summit_name" in args:
        pipeline.create(args)
    elif "query_pipeline_id" in args:
        pipeline.query(args)
    elif "stop_pipeline_id" in args:
        if not args.force:
            # 二次确认
            if not click.confirm('Do you want to continue?', default=False):
                log.info('Aborted.')
                return
            log.info('Confirmed.')
        pipeline.stop(args)
    else:
        pass
