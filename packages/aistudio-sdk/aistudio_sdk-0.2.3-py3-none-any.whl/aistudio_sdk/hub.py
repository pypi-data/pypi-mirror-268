# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
################################################################################
#
# Copyright (c) 2023 Baidu.com, Inc. All Rights Reserved
#
################################################################################
"""
本文件实现了模型库hub接口封装

TODO: 
    当前脚本后续将移动至sdk目录下, 但用法将发生变化, 需和pm确认
    旧：
        from aistudio_sdk.hub import create_repo
        create_repo()
    新：
        from aistudio_sdk import hub
        hub.create_repo()

Authors: linyichong(linyichong@baidu.com)
Date:    2023/08/21
"""
import os
import logging
import traceback
from pathlib import Path
from urllib.parse import quote
from aistudio_sdk.constant.err_code import ErrorEnum
from aistudio_sdk.requests.hub import request_aistudio_hub
from aistudio_sdk.requests.hub import request_aistudio_git_download
from aistudio_sdk.requests.hub import request_aistudio_git_file_info
from aistudio_sdk.requests.hub import request_aistudio_git_file_type
from aistudio_sdk.requests.hub import request_aistudio_git_upload_access
from aistudio_sdk.requests.hub import request_bos_upload
from aistudio_sdk.requests.hub import request_aistudio_git_upload_pointer
from aistudio_sdk.requests.hub import request_aistudio_git_upload_common
from aistudio_sdk.requests.hub import get_exist_file_old_sha
from aistudio_sdk.requests.hub import request_aistudio_repo_visible
from aistudio_sdk.requests.hub import request_aistudio_verify_lfs_file
from aistudio_sdk.utils.util import convert_to_dict_object, is_valid_host, calculate_sha256
from aistudio_sdk.utils.util import err_resp
from aistudio_sdk import config


__all__ = [
    "create_repo",
    "download",
    "upload",
    "file_exists"
]

class UploadFileException(Exception):
    """
    上传文件异常
    """
    pass

class Hub():
    """Hub类"""
    OBJECT_NAME = "hub"

    def __init__(self):
        """初始化函数，从本地磁盘加载AI Studio认证令牌。
        
        Args:
            无参数。
        
        Returns:
            无返回值。
        """

        # 当用户已经设置了AISTUDIO_ACCESS_TOKEN环境变量，那么优先读取环境变量，忽略本地磁盘存的token
        # 未设置时才读存本地token
        if not os.getenv("AISTUDIO_ACCESS_TOKEN", default=""):
            cache_home = os.getenv("AISTUDIO_CACHE_HOME", default=os.getenv("HOME"))
            token_file_path = f'{cache_home}/.cache/aistudio/.auth/token'
            if os.path.exists(token_file_path):
                with open(token_file_path, 'r') as file:
                    os.environ["AISTUDIO_ACCESS_TOKEN"] = file.read().strip()


    def create_repo(self, **kwargs):
        """
        创建一个repo仓库并返回创建成功后的信息。
        """
        # 参数检查
        str_params_not_valid = 'params not valid.'
        if "repo_id" not in kwargs:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message)

        if 'private' in kwargs and kwargs['private'] not in (True, False):
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message)
        for key in ['repo_id', 'model_name', 'license', 'token']:
            if key in kwargs:
                if type(kwargs[key]) != str:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message)
                kwargs[key] = kwargs[key].strip()
                if not kwargs[key]:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message)

        if not os.getenv("AISTUDIO_ACCESS_TOKEN") and 'token' not in kwargs:
            return err_resp(ErrorEnum.TOKEN_IS_EMPTY.code,
                            ErrorEnum.TOKEN_IS_EMPTY.message)

        if 'desc' in kwargs \
                and type(kwargs['desc']) != str:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message)

        # 兼容 带前缀的入参写法
        repo_name_raw = kwargs['repo_id']
        if "/" in repo_name_raw:
            user_name, repo_name = repo_name_raw.split('/')
            user_name = user_name.strip()
            repo_name = repo_name.strip()
            if not repo_name or not user_name:
                return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                ErrorEnum.PARAMS_INVALID.message)
            kwargs['repo_id'] = repo_name
        else:
            kwargs['repo_id'] = repo_name_raw

        params = {
            'repoType': 0 if kwargs.get('private') else 1,
            'repoName': kwargs['repo_id'],
            'modelName': kwargs['model_name'] if kwargs.get('model_name') else kwargs['repo_id'],
            'desc': kwargs.get('desc', ''),
            'license': kwargs['license'].strip() if kwargs.get('license') else 'Apache License 2.0',
            'token': kwargs['token'] if 'token' in kwargs else ''
        }
        resp = convert_to_dict_object(request_aistudio_hub(**params))
        if 'errorCode' in resp and resp['errorCode'] != 0:
            if "repo already created" in resp['errorMsg']:
                res = err_resp(ErrorEnum.REPO_ALREADY_EXIST.code, 
                               resp['errorMsg'],
                               resp['errorCode'],
                               resp['logId'])  # 错误logid透传
            else:
                res = err_resp(ErrorEnum.AISTUDIO_CREATE_REPO_FAILED.code, 
                               resp['errorMsg'],
                               resp['errorCode'],
                               resp['logId'])
            return res

        res = {
            'model_name': resp['result']['modelName'],
            'repo_id': resp['result']['repoName'],
            'private': True if resp['result']['repoType'] == 0 else False,
            'desc': resp['result']['desc'],
            'license': resp['result']['license']
        }
        return res


    def download(self, **kwargs):
        """
        下载:
        params:
            repo_id: 仓库id，格式为user_name/repo_name
            filename: 仓库中的文件路径
            cache_dir: 下载后存放的目录，会存放一个软链接文件
            revision: 分支名
            token: 认证令牌
        """
        # 参数检查
        str_params_not_valid = 'params not valid.'
        if "repo_id" not in kwargs or "filename" not in kwargs:
            return err_resp(ErrorEnum.PARAMS_INVALID.code,
                            ErrorEnum.PARAMS_INVALID.message + "should provide param repo_id and filename")

        for key in ['filename', 'repo_id', 'revision', 'cache_dir', 'token']:
            if key in kwargs:
                if type(kwargs[key]) != str:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message + "should be str type: " + key)
                kwargs[key] = kwargs[key].strip()
                if not kwargs[key]:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message + "should not be empty: " + key)
        revision = kwargs['revision'] if kwargs.get('revision') else 'master'
        file_path = kwargs['filename']
        token = kwargs['token'] if 'token' in kwargs else ''

        repo_name = kwargs['repo_id']
        if "/" not in repo_name:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message + "repo_name should be user_name/repo_name format.")

        user_name, repo_name = repo_name.split('/')
        user_name = user_name.strip()
        repo_name = repo_name.strip()
        if not repo_name or not user_name:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message + "repo_name or user_name is empty.")

        git_host = os.getenv("STUDIO_GIT_HOST", default=config.STUDIO_GIT_HOST_DEFAULT)
        if not is_valid_host(git_host):
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            'host not valid.')

        # 检查仓库可见权限(他人的预发布仓库不能下载、查看)
        if os.environ.get("SKIP_REPO_VISIBLE_CHECK", default="false") != "true":
            params = {
                'repoId': kwargs['repo_id'],
                'token': kwargs['token'] if 'token' in kwargs else ''
            }
            resp = convert_to_dict_object(request_aistudio_repo_visible(**params))
            if 'errorCode' in resp and resp['errorCode'] != 0:
                res = err_resp(ErrorEnum.AISTUDIO_NO_REPO_READ_AUTH.code,
                                resp['errorMsg'],
                                resp['errorCode'],
                                resp['logId'])
                return res

        # 查询文件sha值
        info_res = request_aistudio_git_file_info(git_host, user_name, repo_name, file_path,
                                                  revision, token)
        if 'error_code' in info_res and info_res['error_code'] != ErrorEnum.SUCCESS.code:
            return info_res
        file_sha = info_res['sha']

        # 构建source_path
        home = os.getenv("HOME")
        cache_home = os.getenv("AISTUDIO_CACHE_HOME", default=home)
        source_dir = Path(f"{cache_home}/.cache/aistudio/models/{repo_name}/blobs")
        source_path = Path(f"{source_dir}/{file_sha}")

        # 检查目标文件是否已下载
        if os.path.exists(source_path):
            print("The file already exists, skip the download.")
        else:
            # 创建下载文件目录
            os.makedirs(source_dir, exist_ok=True)
            url = (
                f"{git_host}/api/v1/repos/"
                f"{quote(user_name, safe='')}/"
                f"{quote(repo_name, safe='')}/media/"
                f"{quote(file_path, safe='')}")
            if revision != 'master':
                url += f"?ref={quote(revision, safe='')}"
            download_res = request_aistudio_git_download(url, source_path, token)
            if 'error_code' in download_res and download_res['error_code'] != ErrorEnum.SUCCESS.code:
                return download_res

        # 构建软链接的路径
        if 'cache_dir' in kwargs:
            cache_dir = kwargs['cache_dir']
            target_dir = Path(cache_dir)
        else:
            commit_id = info_res['last_commit_sha']
            target_dir = Path(f"{cache_home}/.cache/aistudio/models/{repo_name}/snapshots/{revision}/{commit_id}")  
        target_path = Path(f"{target_dir}/{file_path}")

        # 删掉已经存在的软链接文件
        if os.path.exists(target_path):
            os.unlink(target_path)

        # 预创建软链接文件所在目录
        parsed_path = Path(file_path)
        prefix_path = parsed_path.parent
        os.makedirs(os.path.join(target_dir, prefix_path), exist_ok=True)

        # 创建符号链接（软链接）
        if os.name == "nt":  # Windows系统  
            # 使用不同的命令来创建目录链接和文件链接
            if os.path.isdir(source_path):
                os.system(f"mklink /D \"{target_path}\" \"{source_path}\"")
            else:
                os.system(f"mklink \"{target_path}\" \"{source_path}\"")
        else:  # 非Windows系统（如Linux）
            os.symlink(source_path, target_path) 

        return {'path': f"{target_path}"}

    def _upload_lfs_file(self, settings, file_path, file_size):
        """
        上传文件
        settings: 上传文件的配置信息
        settings = {
            'upload'[bool]: True or False
            'upload_href'[str]:  upload url
            'sts_token'[dict]: sts token
                {
                "bos_host":"",
                "bucket_name": "",
                "key":"",
                "access_key_id": "",
                "secret_access_key": "",
                "session_token": "",
                "expiration": ""
                }
        }
        file_path: 本地文件路径
        """
        if not settings.get('upload'):
            logging.info("file already exists, skip the upload.")
            return True

        upload_href = settings['upload_href']
        sts_token = settings.get('sts_token', {})
        is_sts_valid = False
        if sts_token and sts_token.get("bos_host"):
            is_sts_valid = True

        is_http_valid = True if upload_href and file_size < config.LFS_FILE_SIZE_LIMIT_PUT else False

        def _uploading_using_sts():
            """
            使用sts上传文件
            """
            from aistudio_sdk.utils.bos_sdk import sts_client, upload_file, upload_super_file
            try:
                client = sts_client(sts_token.get("bos_host"), sts_token.get("access_key_id"),
                           sts_token.get("secret_access_key"), sts_token.get("session_token"))
                res = upload_super_file(client,
                                        bucket=sts_token.get("bucket_name"), file=file_path, key=sts_token.get("key"))
                return res
            except Exception as e:
                raise UploadFileException(e)


        def _uploading_using_http():
            """
            使用http上传文件
            """
            try:
                res = request_bos_upload(upload_href, file_path)
                if 'error_code' in res and res['error_code'] != ErrorEnum.SUCCESS.code:
                    return res
                return True
            except Exception as e:
                raise UploadFileException(e)

        functions = []
        if is_sts_valid:
            functions.append(_uploading_using_sts)
        if is_http_valid:
            functions.append(_uploading_using_http)
        if not os.environ.get("PERFER_STS_UPLOAD", default="true") == "true":
            functions.reverse()
        if not functions:
            logging.error("no upload method available.")
            return False

        upload_success = False
        for func in functions:
            try:
                logging.info(f"uploading file using {func.__name__}")
                res = func()
                if res is True:
                    logging.info(f"upload lfs file success. {func.__name__}")
                    upload_success = True
                    break
                else:
                    logging.error(f"upload lfs file failed. {func.__name__}: {res}")
            except UploadFileException as e:
                logging.error(f"upload lfs file failed. {func.__name__}: {e}")
                logging.debug(traceback.format_exc())

        return upload_success


    def upload(self, **kwargs):
        """
        上传
        params:
            repo_id: 仓库id，格式为user_name/repo_name
            path_or_fileobj: 本地文件路径或文件对象
            path_in_repo: 上传的仓库中的文件路径
            revision: 分支名
            commit_message: 提交信息
            token: 认证令牌
        return:
            message
        """
        # 参数检查
        str_params_not_valid = 'params not valid.'
        if "repo_id" not in kwargs or "path_or_fileobj" not in kwargs or "path_in_repo" not in kwargs:
            return err_resp(ErrorEnum.PARAMS_INVALID.code,
                            ErrorEnum.PARAMS_INVALID.message 
                            + "should provide param repo_id, path_or_fileobj and path_in_repo")

        for key in ['path_or_fileobj', 'repo_id', 'revision', 'path_in_repo', 
                    'commit_message', 'token']:
            if key in kwargs:
                if type(kwargs[key]) != str:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message + "should be str type: " + key)
                kwargs[key] = kwargs[key].strip()
                if not kwargs[key]:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message + "should not be empty: " + key)

        if not os.getenv("AISTUDIO_ACCESS_TOKEN") and 'token' not in kwargs:
            return err_resp(ErrorEnum.TOKEN_IS_EMPTY.code,
                            ErrorEnum.TOKEN_IS_EMPTY.message)

        revision = kwargs['revision'] if kwargs.get('revision') else 'master'
        commit_message = kwargs['commit_message'] if kwargs.get('commit_message') else ''
        token = kwargs['token'] if kwargs.get('token') else ''

        path_or_fileobj = Path(kwargs['path_or_fileobj'])
        path_in_repo = kwargs['path_in_repo']

        repo_id = kwargs['repo_id']
        if "/" not in repo_id:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message + "repo_name should be user_name/repo_name format.")

        user_name, repo_name = repo_id.split('/')
        user_name = user_name.strip()
        repo_name = repo_name.strip()
        if not repo_name or not user_name:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message + "repo_name or user_name is empty.")

        git_host = os.getenv("STUDIO_GIT_HOST", default=config.STUDIO_GIT_HOST_DEFAULT)
        if not is_valid_host(git_host):
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            'git host not valid.')

        # 检查待上传文件在本地磁盘是否存在
        if not os.path.exists(path_or_fileobj):
            return err_resp(ErrorEnum.UPLOAD_FILE_NOT_FOUND.code,
                            'file not found in path. ' + str(path_or_fileobj))

        # 检查待上传文件类型，不能是folder（目录）
        if os.path.isdir(path_or_fileobj):
            return err_resp(ErrorEnum.UPLOAD_FOLDER_NO_SUPPORT.code,
                            'upload folder no support.' + str(path_or_fileobj))

        # 计算文件大小（byte）
        file_size = os.path.getsize(path_or_fileobj)

        
        # 第一步: 检查文件是否需要走LFS上传流程
        print("checking is file using lfs ..")
        res = request_aistudio_git_file_type(git_host, user_name, repo_name,
                                             revision, path_in_repo, token)
        if 'error_code' in res and res['error_code'] != ErrorEnum.SUCCESS.code:
            return res
        is_lfs = res['is_lfs']

        # 计算sha256
        sha256 = calculate_sha256(path_or_fileobj)

        if is_lfs:
            print("Start uploading LFS file.")
            # 第二步：申请上传LFS文件

            res = request_aistudio_git_upload_access(git_host, user_name, repo_name, revision,
                                                     file_size, sha256, token)
            logging.debug(f"request_aistudio_git_upload_access res: {res}")
            if 'error_code' in res and res['error_code'] != ErrorEnum.SUCCESS.code:
                return res

            # 第三步：上传LFS文件
            if res.get('upload'):

                upload_res = self._upload_lfs_file(res, path_or_fileobj, file_size)
                if not upload_res:
                    logging.error("upload lfs file failed. 文件上传终止")
                    return err_resp(ErrorEnum.GITEA_UPLOAD_FILE_FAILED.code, 
                                    f"lfs {ErrorEnum.GITEA_UPLOAD_FILE_FAILED.message}")

            else:
                # bos存储中该文件已存在。只需要再创建一次指针文件到指定分支即可。
                pass

            # 第四步：verify LFS file（判断文件是否存在）
            if res.get("verify_href"):
                verify_res = request_aistudio_verify_lfs_file(res.get("verify_href"), sha256, file_size)
                logging.info(f"verify lfs file res: {verify_res}")
                if 'error_code' in verify_res and verify_res['error_code'] != ErrorEnum.SUCCESS.code:
                    logging.error("verify lfs file failed. 文件上传终止")
                    return verify_res

            # 第五步：上传LFS指针文件（到仓库）
            lfs_res = request_aistudio_git_upload_pointer(git_host, user_name, repo_name, revision,
                                                    commit_message, sha256, file_size, path_in_repo,
                                                    token)
            if 'error_code' in lfs_res and lfs_res['error_code'] != ErrorEnum.SUCCESS.code:
                return lfs_res
            logging.info(f"upload lfs pointer file success")

        else:
            print("Start uploading common file.")
            # 如果大小超标，报错返回
            if file_size > config.COMMON_FILE_SIZE_LIMIT:
                return err_resp(ErrorEnum.FILE_TOO_LARGE.code,
                                ErrorEnum.FILE_TOO_LARGE.message + '(>5MB).')

            # 上传普通文件（到仓库）
            res = request_aistudio_git_upload_common(git_host, user_name, repo_name, revision,
                                                     commit_message, path_or_fileobj, path_in_repo,
                                                     token)
            if 'error_code' in res and res['error_code'] != ErrorEnum.SUCCESS.code:
                return res

        return {'message': 'Upload Done.'}


    def file_exists(self, repo_id, filename, *args, **kwargs):
        """
        文件是否存在
        params:
            repo_id: 仓库id，格式为user_name/repo_name
            filename: 仓库中的文件路径
            revision: 分支名
            token: 认证令牌
        """
        # 参数检查
        str_params_not_valid = 'params not valid.'
        kwargs['repo_id'] = repo_id
        kwargs['filename'] = filename

        # 检查入参值的格式类型
        for key in ['filename', 'repo_id', 'revision', 'token']:
            if key in kwargs:
                if type(kwargs[key]) != str:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message)
                kwargs[key] = kwargs[key].strip()
                if not kwargs[key]:
                    return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                                    ErrorEnum.PARAMS_INVALID.message)
        revision = kwargs['revision'] if kwargs.get('revision') else 'master'
        file_path = kwargs['filename']
        token = kwargs['token'] if 'token' in kwargs else ''

        repo_name = kwargs['repo_id']
        if "/" not in repo_name:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message)

        user_name, repo_name = repo_name.split('/')
        user_name = user_name.strip()
        repo_name = repo_name.strip()
        if not repo_name or not user_name:
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            ErrorEnum.PARAMS_INVALID.message)

        call_host = os.getenv("STUDIO_GIT_HOST", default=config.STUDIO_GIT_HOST_DEFAULT)
        if not is_valid_host(call_host):
            return err_resp(ErrorEnum.PARAMS_INVALID.code, 
                            'host not valid.')

        if os.environ.get("SKIP_REPO_VISIBLE_CHECK", default="false") != "true":
            # 检查仓库可见权限(他人的预发布仓库不能下载、查看)
            params = {
                'repoId': kwargs['repo_id'],
                'token': kwargs['token'] if 'token' in kwargs else ''
            }
            resp = convert_to_dict_object(request_aistudio_repo_visible(**params))
            if 'errorCode' in resp and resp['errorCode'] != 0:
                res = err_resp(ErrorEnum.AISTUDIO_NO_REPO_READ_AUTH.code,
                                resp['errorMsg'],
                                resp['errorCode'],
                                resp['logId'])
                return res

        # 查询文件是否存在
        info_res = request_aistudio_git_file_info(call_host, user_name, repo_name, file_path, 
                                                  revision, token)
        if get_exist_file_old_sha(info_res) == '':
            return False
        else:
            return True


def create_repo(**kwargs):
    """
    创建
    """
    return Hub().create_repo(**kwargs)


def download(**kwargs):
    """
    下载
    """
    return Hub().download(**kwargs)


def upload(**kwargs):
    """
    上传
    """
    return Hub().upload(**kwargs)


def file_exists(repo_id, filename, *args, **kwargs):
    """
    检查云端文件存在与否
    """
    return Hub().file_exists(repo_id, filename, *args, **kwargs)
