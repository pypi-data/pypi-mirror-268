#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
from zabbix_api import ZabbixAPI, ZabbixAPIException
from diskcache import Cache

ZABBIX_TIMEOUT = int(os.environ.get("WXZBXASSISTANT_ZABBIX_API_TIMEOUT", 60))
cache = Cache(".cache")


class ZabbixAPIS:
    def __init__(self, login_user: str = ""):
        self.__url = os.environ.get("WXZBXASSISTANT_ZABBIX_URL")
        self.__username = os.environ.get("WXZBXASSISTANT_ZABBIX_USERNAME")
        self.__api_token = os.environ.get("WXZBXASSISTANT_ZABBIX_API_TOKEN")
        self.__login_user = login_user.strip()
        self._zbx_api = None
        self._user_zbx_api = None

    @property
    def url(self):
        """Zabbix Server URL"""
        return self.__url

    @property
    def username(self):
        """Zabbix Server Login Username"""
        return self.__username

    @property
    def api_token(self):
        """Zabbix User API Token"""
        return self.__api_token

    @property
    def login_user(self):
        """Wxwork Login User"""
        return self.__login_user

    @property
    def zbxapi(self):
        """
            封装【管理员用户】的 Zabbix Json RPC 调用：
                1. zabbix_api 库提供了一个 ZabbixAPI 类，它封装了对 Zabbix 服务器的 JSON RPC 调用；
        :return:
        """
        if self._zbx_api:
            return self._zbx_api
        try:
            zbx_api = ZabbixAPI(server=self.url, timeout=ZABBIX_TIMEOUT)
            # 与 Zabbix API 进行 HTTPS 通信时，【不验证 SSL 证书的有效性】
            # 在连接的 Zabbix API 服务器使用【自签名证书】或者希望【忽略由于某些原因引起的证书验证问题】时有用
            zbx_api.validate_certs = False
            zbx_api.login(user=self.username, api_token=self.api_token)
            self._zbx_api = zbx_api
            return self._zbx_api
        except ZabbixAPIException as err:
            logging.error(str(err))

    @property
    def zbx_user(self):
        """
            根据登录用户企业微信 User ID 过滤出对应的 Zabbix User 信息:
                1. 企业微信和 Zabbix 监控系统并无直接关联，但是在 Zabbix
                   中在配置用户的告警媒介时可以选择配置企业微信告警媒介；
                2. 用户的企业微信告警媒介的 "sendto" 字段中包含有用户企业微信 User ID。
        :return:
        """
        cached_user_key = f"WxZbxAssistant_WxWork_{self.login_user}"
        cached_user = cache.get(cached_user_key)
        if cached_user:
            return cached_user
        try:
            users = self.zbxapi.user.get(
                {
                    "output": ["userid", "username"],
                    "selectMedias": ["sendto"]
                }
            )
            for user in users:
                for media in user.get("medias", []):
                    if self.login_user in media.get("sendto", ""):
                        matched_user = (user.get("userid"), user.get("username"))
                        cache.set(cached_user_key, matched_user)
                        return cache.get(cached_user_key)
        except ZabbixAPIException as err:
            logging.error(msg=str(err))

    @property
    def token_name(self):
        """Zabbix 用户的默认 Token 规范名称"""
        return f"WxZbxAssistant_{self.zbx_user[1]}"

    @property
    def user_token_page(self):
        """获取 Zabbix 用户页面上的 token"""
        try:
            tokens = self.zbxapi.token.get(
                {
                    "filter": {
                        "name": self.token_name
                    }
                }
            )
            return tokens
        except ZabbixAPIException as err:
            logging.error(str(err))

    def create_zbx_user_token(self):
        """
            创建 Zabbix 用户 Token：
        :return:
        """
        tokenids = self.zbxapi.token.create(
            {
                "name": self.token_name,
                "userid": self.zbx_user[0]
            }
        )
        tokens = self.zbxapi.token.generate(
            [tokenids.get("tokenids")[0]]
        )
        if tokens[0].get("token"):
            cache.set(
                self.token_name,
                {
                    "tokenid": tokens[0].get("tokenid"),
                    "token": tokens[0].get("token")
                }
            )
        return cache.get(self.token_name).get("token")

    @property
    def user_token(self):
        """
            创建企业微信登录用户对应的 Zabbix 用户的 token：
                1. API Tokens 信息存在于 Zabbix 用户的个人设置项中，可以手动创建，
                   也可以通过 API 创建，通过 API 创建则需要管理员权限；
                2. token 一旦被创建则不再改变，但是用户个人页面上必须存在相应的 token 记录，
                   如果被删除则会失效。
        :return:
        """
        if self.user_token_page and cache.get(self.token_name):
            return cache.get(self.token_name).get("token")
        if self.zbx_user and not self.user_token_page:
            return self.create_zbx_user_token()
        if self.user_token_page and not cache.get(self.token_name):
            self.zbxapi.token.delete([self.user_token_page[0].get("tokenid")])
            return self.create_zbx_user_token()
        if not self.user_token_page and cache.get(self.token_name):
            cache.delete(self.token_name)
            return self.create_zbx_user_token()

    @property
    def user_zbxapi(self):
        """
            封装【登录用户(即普通用户)】的 Zabbix Json RPC 调用：
                1. 企业微信用户登录之后，后台获取到其对应的 Zabbix User ID，通过管理员用户生成其 Token，
                   然后使用 Zabbix User 用户名及其 Token 重新封装 API，基于此进行后续的操作。
        :return:
        """
        if self._user_zbx_api:
            return self._user_zbx_api
        try:
            # Zabbix 页面上的用户 Token 须和缓存中的 Token 是同一个，否则认证失败
            if (self.user_token_page and cache.get(self.token_name) and
                    self.user_token_page[0].get("tokenid") != cache.get(self.token_name).get("tokenid")):
                cache.delete(self.token_name)
            user_id = self.zbx_user[0]
            token = self.user_token
            if user_id and token:
                zbx_api = ZabbixAPI(server=self.url, timeout=ZABBIX_TIMEOUT)
                # 与 Zabbix API 进行 HTTPS 通信时，【不验证 SSL 证书的有效性】
                # 在连接的 Zabbix API 服务器使用【自签名证书】或者希望【忽略由于某些原因引起的证书验证问题】时有用
                zbx_api.validate_certs = False
                zbx_api.login(user=user_id, api_token=token)
                self._user_zbx_api = zbx_api
                return self._user_zbx_api
        except ZabbixAPIException as err:
            logging.error(msg=str(err))
