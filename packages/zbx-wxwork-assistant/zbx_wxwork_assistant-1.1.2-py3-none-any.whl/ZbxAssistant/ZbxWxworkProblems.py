#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from ast import literal_eval
from datetime import datetime, timedelta
import logging
from zabbix_api import ZabbixAPIException
from .ZbxApis import ZabbixAPIS
from .ZbxConfigs import ACKNOWLEDGED, SUPPRESSED, SEVERITY

ZABBIX_SEVERITIES = list(literal_eval(os.environ.get("WXZBXASSISTANT_ZABBIX_SEVERITIES"))) \
    if os.environ.get("WXZBXASSISTANT_ZABBIX_SEVERITIES") \
    else [0, 1, 2, 3, 4, 5]


class ZabbixProblems(ZabbixAPIS):
    def __init__(self, login_user: str = ""):
        super().__init__(login_user)
        self._login_user = login_user.strip()

    def get_trigger_lastvalue(self, objectid: str):
        """
            获取 Zabbix 告警的最新告警值：
                1. 在 Zabbix API 中，objectid 通常指的是与问题（problem）相关联的实体的唯一标识符；
                2. 这个实体可能是触发器（trigger）、项目（item）或者图形（graph）等；
                3. 这个问题如果是由触发器引起的，那么 objectid 就是那个触发器的 ID。
        :param objectid:
        :return:
        """
        if self.user_zbxapi:
            trigger = self.user_zbxapi.trigger.get(
                {
                    "triggerids": objectid,
                    "selectItems": ["lastvalue"]
                }
            )
            items = trigger[0].get("items")
            return items[0].get("lastvalue") if trigger and items else None

    def __format_problem(self, problem: dict, host_interfaces: list, host_name: str):
        """
            格式化问题数据：
                1. 将 Zabbix 问题（告警）的相关信息进行格式化，包括时间格式的转换、
                   确认状态、抑制状态和严重性级别的解析，并获取触发器的最后值。
                2. 格式化过程中，会对以下字段进行处理：
                       - "clock": 将 Unix 时间戳转换为 "YYYY-MM-DD HH:MM:SS" 格式，并假设是 UTC+8 时区
                       - "acknowledged": 解析并返回确认状态描述
                       - "suppressed": 解析并返回抑制状态描述
                       - "severity": 解析并返回严重性级别描述
                       - "lastvalue": 获取并返回关联触发器的最后值
                       - "host": 如果提供了 host_name，则使用 host_name；否则，将 host_interfaces 列表转换为字符串
        :param problem:
        :param host_interfaces:
        :param host_name:
        :return:
        """
        date = datetime.utcfromtimestamp(int(problem.get("clock"))) + timedelta(hours=8)
        problem["clock"] = date.strftime("%Y-%m-%d %H:%M:%S")
        problem["acknowledged"] = ACKNOWLEDGED.get(
            problem.get("acknowledged"), "").split(r"/", maxsplit=1)[0]
        problem["suppressed"] = SUPPRESSED.get(
            problem.get("suppressed"), "").split(r"/", maxsplit=1)[0]
        problem["severity"] = SEVERITY.get(
            problem.get("severity"), "").split(r"/", maxsplit=1)[0]
        problem["lastvalue"] = self.get_trigger_lastvalue(objectid=problem.get("objectid"))
        problem["host"] = host_name or ", ".join(host_interfaces)
        return problem

    def __format_problems(self, problems: list, host: dict):
        """
            格式化问题列表，为每个问题生成一个格式化后的表示：
                1. 遍历输入的问题列表，对每一个问题调用 __format_problem() 方法进行格式化，
                   同时利用提供的主机信息生成该主机对应的名称，并将其与问题信息一起整合返回。
        :param problems:
        :param host:
        :return:
        """
        interfaces = [
            inf.get("ip")
            for inf in host.get("interfaces", [])
            if inf
        ]
        host_name = host.get("name") or host.get("host") or ", ".join(interfaces)
        return [
            self.__format_problem(
                problem=problem,
                host_interfaces=interfaces,
                host_name=host_name
            )
            for problem in problems
        ]

    def get_zbx_problems(self, host: dict, severities=None, **kwargs):
        """
            根据传入的 Zabbix 主机信息获取【此主机最近发生的告警信息】：
                1. "recent" 为 True 时，返回问题和最近解决的问题；
                   "recent" 为 False 时，仅返回未解决的问题。
        :param host:
        :param severities:
        :param kwargs:
        :return:
        """
        if severities is None:
            severities = ZABBIX_SEVERITIES
        try:
            if self.user_zbxapi:
                problems = self.user_zbxapi.problem.get(
                    {
                        "output": [
                            "eventid",
                            "objectid",
                            "clock",
                            "name",
                            "acknowledged",
                            "severity",
                            "r_clock",
                            "suppressed"
                        ],
                        "hostids": host.get("hostid"),
                        "severities": severities,
                        **{
                            k: v
                            for k, v in kwargs.items()
                            if k in ["recent", "acknowledged", "suppressed"]
                        }
                    }
                )
                return self.__format_problems(problems=problems, host=host)
        except ZabbixAPIException as err:
            logging.error(str(err))
            return []

    def fetch_problems(self, host: dict, severities=None, **kwargs):
        """
            使用多线程/多进程的非迭代传入来获取主机告警信息：
        :param host:
        :param severities:
        :param kwargs:
        :return:
        """
        return self.get_zbx_problems(
            host=host,
            severities=severities,
            **kwargs
        )
