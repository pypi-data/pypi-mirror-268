import json
from datetime import datetime

from dateutil.tz import tz
from requests import Response

from .file_manager import LogFileManager
import time
import requests

TZ_NAME = 'Asia/Shanghai'
ERROR_MSG = """
---------------------------------- {0} begin ----------------------------------
请求URL是：{1}
请求headers是：{2}
请求params是：{3}
请求post是：{4}
错误信息是：{5}
---------------------------------- {0} end ----------------------------------
"""


class ApiClient(requests.Session):
    def __init__(self, node_id: str, retry_count: int, timeout: int, host: str):
        """
        初始化API客户端基类
        :param node_id 节点ID
        :param retry_count 重试次数
        :param timeout 请求超时时间
        :param host 域名地址
        """
        super(ApiClient, self).__init__()
        self.retry_count = retry_count
        self.node_id = node_id
        self.timeout = timeout
        self.host = host

    def res_callback(self, res_data: Response):
        """
        响应回调
        :param res_data 响应数据
        """
        return res_data

    def try_get(self, url, error_count: int = 0, e='', **kwargs):
        """
        尝试重发get请求
        """
        while error_count <= self.retry_count:
            try:
                res_data = self.get(url, timeout=self.timeout, **kwargs)
                return self.res_callback(res_data)
            except Exception as e:
                print(e)
                time.sleep(error_count)
                error_count += 1
                return self.try_get(url, error_count, e, **kwargs)
        raise Exception('已经尝试请求：{}次，服务器依然没有响应，错误信息是：{}'.format(self.retry_count, str(e)))

    def try_post(self, url: str, error_count: int = 0, e='', **kwargs):
        """
        尝试重发post请求
        """
        while error_count <= self.retry_count:
            try:
                res_data = self.post(url, timeout=self.timeout, **kwargs)
                return self.res_callback(res_data)
            except Exception as e:
                print(e)
                time.sleep(error_count)
                error_count += 1
                time.sleep(error_count)
                return self.try_post(url, error_count, e, **kwargs)
        raise Exception('已经尝试请求：{}次，服务器依然没有响应，错误信息是：{}'.format(self.retry_count, str(e)))

    @staticmethod
    def get_log_time():
        """
        生成日志时间
        """
        now_datetime_obj = datetime.fromtimestamp(int(time.time()), tz.gettz(TZ_NAME))
        return str(now_datetime_obj).replace(' ', 'T', 1)

    @staticmethod
    def get_log_id() -> str:
        """
        生成日志ID
        """
        return str(time.time()).replace('.', '')


class MigoApiClient(ApiClient):
    def __init__(self, node_id: str, retry_count: int, timeout: int, host: str, auth_key: str, log_path: str):
        """
        初始化米果API客户端
        :param node_id 节点ID
        :param retry_count 重试次数
        :param timeout 请求超时时间
        :param host
        :param auth_key 认证key
        :param log_path 日志路径
        """
        super(MigoApiClient, self).__init__(node_id, retry_count, timeout, host)
        self.auth_key = auth_key
        self.headers = {
            'AUTH-KEY': auth_key,
            'CURRENT-USER-NAME': 'system',
            'CURRENT-USER-ID': '100001'
        }
        self.log_manager = LogFileManager(log_path)

    def res_callback(self, res: Response):
        """
        响应回调
        """
        response_data = res.json()
        if response_data['code'] != 200:
            raise Exception(response_data['message'])
        return response_data

    def migo_try_get(self, url, migo_shop_id, data_type: str, error_count: int = 0, **kwargs):
        """
        自定义发get请求
        :param url 链接
        :param migo_shop_id 米果店铺ID
        :param data_type 数据类型
        :param error_count 重试次数
        """
        try:
            return self.try_get(url, error_count, **kwargs)
        except Exception as e:
            log_params = kwargs.get('params', {})
            log_data = kwargs['json'] if kwargs.get('json', {}) else kwargs.get('data', {})
            self.post_error_log(str(e), data_type, migo_shop_id, log_data, log_params)
            raise e

    def migo_try_post(self, url, migo_shop_id, data_type: str, error_count: int = 0, **kwargs):
        """
        自定义发post请求
        :param url 链接
        :param migo_shop_id 米果店铺ID
        :param data_type 数据类型
        :param error_count 重试次数
        """
        try:
            return self.try_post(url, error_count, **kwargs)
        except Exception as e:
            log_params = kwargs.get('params', {})
            log_data = kwargs['json'] if kwargs.get('json', {}) else kwargs.get('data', {})
            self.post_error_log(str(e), data_type, migo_shop_id, log_data, log_params)
            raise e

    def get_shop_auth(self, migo_shop_id: int):
        """
        获取店铺授权信息
        :param migo_shop_id 米果店铺ID
        """
        uri = f'/data-collection-service/node/auths/{migo_shop_id}'
        return self.migo_try_get(self.host + uri, migo_shop_id, '获取店铺授权信息')

    def get_node_info_list(self, migo_shop_id: int = 0):
        """
        获取节点信息列表
        :param migo_shop_id 米果店铺ID
        """
        post_data = {
            "nodeConfigId": self.node_id,
            "shopId": migo_shop_id
        }
        uri = f'/data-collection-service/node/search'
        response_data = self.migo_try_post(self.host + uri, migo_shop_id, '获取节点信息列表', json=post_data)
        if migo_shop_id:
            response_data['data'] = response_data['data'][0]  # 如果是查询单个店铺的话，数据解析成字典
        return response_data

    def post_auth_data(self, migo_shop_id, **kwargs):
        """
        刷新认证数据
        :param migo_shop_id 米果店铺ID
        :param kwargs 所需的认证参数
        """
        post_data = {
            "crawlData": json.dumps(kwargs),
            "nodeConfigId": self.node_id,
            "shopId": migo_shop_id
        }
        uri = '/data-collection-service/node/refresh'
        return self.migo_try_post(self.host + uri, migo_shop_id, '刷新认证数据', json=post_data)

    def post_crawl_data(self, crawl_data: dict, data_type: str, migo_shop_id: str):
        """
        推送采集数据
        :param crawl_data 采集数据
        :param data_type 业务类型，订单或物流或其他
        :param migo_shop_id 店铺ID
        """
        uri = '/data-collection-service/node/save'
        # 自动修正丢失的店铺ID
        if 'shopId' not in crawl_data:
            crawl_data['shopId'] = migo_shop_id

        if 'tableName' not in crawl_data:
            msg = '表名不能为空'
            self.post_error_log(msg, data_type, migo_shop_id, crawl_data)
            raise Exception(msg)
        return self.migo_try_post(self.host + uri, migo_shop_id, data_type + '推送采集数据', 0, json=crawl_data)

    def get_heartbeat(self):
        """
        发送心跳
        """
        uri = f'/data-collection-service/node/heartbeat/{self.node_id}'
        return self.try_get(self.host + uri, error_count=0)

    def post_error_log(self, error_msg: str, data_type: str, shop_id: str, log_data: dict = None,
                       log_params: dict = None, log_stack: str = None):
        """
        上传日志，如果上传失败就写入到本地日志中
        :param error_msg 错误信息
        :param data_type 数据类型
        :param shop_id 店铺ID
        :param log_data 请求的post参数
        :param log_params 请求的get参数
        :param log_stack 日志其他信息
        """
        uri = '/data-collection-service/node/logsave'
        post_data = {
            "data": [
                {
                    "migoPrimaryKey": self.get_log_id(),  # 日志数据能容忍缺失，所以暂时用时间戳作为ID
                    "shopId": shop_id,
                    "nodeId": self.node_id,
                    "dataType": data_type,
                    "logTime": self.get_log_time(),
                    "logData": json.dumps(log_data),
                    "logParams": json.dumps(log_params),
                    "logStack": log_stack,
                    "logMsg": error_msg
                }
            ],
            "primaryKey": "migoPrimaryKey",
            "refreshNow": 0,
            "tableName": "node_spider_log_error"
        }
        try:
            res_data = self.try_post(self.host + uri, 0, json=post_data)
            return res_data
        except Exception as e:
            msg = ERROR_MSG.format(
                self.get_log_time(),
                self.host + uri,
                self.headers,
                '',
                post_data,
                str(e),
            )
            self.log_manager.write_request_error_log(msg)
            raise e

    def post_info_log(self, msg: str, data_type: str, shop_id: str, log_data: dict = None,
                      log_params: dict = None, log_stack: str = None):
        """
        上传日志
        :param msg 信息
        :param data_type 数据类型
        :param shop_id 店铺ID
        :param log_data 请求的post参数
        :param log_params 请求的get参数
        :param log_stack 日志其他信息
        """
        uri = '/data-collection-service/node/logsave'
        post_data = {
            "data": [
                {
                    "migoPrimaryKey": self.get_log_id(),  # 日志数据能容忍缺失，所以暂时用时间戳作为ID
                    "shopId": shop_id,
                    "nodeId": self.node_id,
                    "dataType": data_type,
                    "logTime": self.get_log_time(),
                    "logData": json.dumps(log_data),
                    "logParams": json.dumps(log_params),
                    "logStack": log_stack,
                    "logMsg": msg
                }
            ],
            "primaryKey": "migoPrimaryKey",
            "refreshNow": 0,
            "tableName": "node_spider_log"
        }
        return self.migo_try_post(self.host + uri, shop_id, '上传日志', 0, json=post_data)

    def post_node_es_query(self, column_list: list, table_name: str, es_query: dict):
        """
        根据es语法获取节点信息
        :param column_list 字段名
        :param table_name 表名
        :param es_query es查询语句
        """
        uri = '/data-collection-service/node/es/query'
        post_data = {
            'sourceStrings': column_list,
            'queryString': json.dumps(es_query),
            'indexName': table_name
        }
        return self.migo_try_post(self.host + uri, 0, '获取节点信息', 0, json=post_data)

    def post_schedule_log(self, msg: str, shop_id: str, definition_info: dict, log_params: dict = None):
        """
        上传日志
        :param msg 信息
        :param shop_id 店铺ID
        :param definition_info 策略信息
        :param log_params 其他信息
        """
        data_type = '更新调度策略'
        return self.post_info_log(msg, data_type, shop_id, definition_info, log_params)

    def post_error_schedule_log(self, msg: str, shop_id: str, definition_info: dict = None, log_params: dict = None):
        """
        上传错误日志
        :param msg 信息
        :param shop_id 店铺ID
        :param definition_info 策略信息
        :param log_params 其他信息
        """
        data_type = '更新调度策略失败'
        return self.post_error_log(msg, data_type, shop_id, definition_info, log_params)
