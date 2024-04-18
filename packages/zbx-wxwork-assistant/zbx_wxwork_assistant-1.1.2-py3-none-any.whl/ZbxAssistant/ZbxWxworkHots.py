#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from zabbix_api import ZabbixAPIException
from .ZbxApis import ZabbixAPIS


class ZabbixHosts(ZabbixAPIS):
    def __init__(self, login_user: str = ""):
        super().__init__(login_user)
        self._login_user = login_user.strip()

    @property
    def hosts(self):
        """
            获取登录用户有权查看的所有主机信息：
                1. 直接使用以登录用户信息封装的 Zabbix API 去获取 Zabbix 主机信息。
        :return:
        """
        try:
            if self.user_zbxapi:
                hosts = self.user_zbxapi.host.get(
                    {
                        "output": [
                            "hostid",
                            "name",
                            "interfaces",
                            "host"
                        ],
                        "selectInterfaces": ["ip"]
                    }
                )
                return hosts
        except ZabbixAPIException as err:
            logging.error(str(err))
