#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# 代表 Zabbix Problem 【是否被确认】的参数表示
ACKNOWLEDGED = {
    "0": "unacknowledged/未确认",
    "1": "acknowledged/确认"
}
# 代表 Zabbix Problem 【是否处于维护状态】的参数表示
SUPPRESSED = {
    "0": "normal/未维护",
    "1": "suppressed/维护中"
}
# 代表 Zabbix Problem 【告警级别】的参数表示
SEVERITY = {
    "0": "Not classified/未分类",
    "1": "Information/信息",
    "2": "Warning/警告",
    "3": "Average/一般严重",
    "4": "High/严重",
    "5": "Disaster/灾难"
}
