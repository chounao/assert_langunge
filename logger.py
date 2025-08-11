#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：logger
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/6 09:50
@ModifyTime    :
"""
import logging

# 创建模块级logger，避免重复创建
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger_instance = logging.getLogger(__name__)

def get_logger():
    """
    获取配置好的logger实例
    """
    return logger_instance
