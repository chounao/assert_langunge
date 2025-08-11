#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：approval page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/7 16:11
@ModifyTime    : 2023/8/8 17:23
"""
# from base_page import BasePage
# import time
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class ApprovalData:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#
#     def  pending_approval_data(self):
#         data = {
#             'path':'/app/pending-approval'
#         }
#         return data
#
#     def approved_data(self):
#         data = {
#             'path':'/app/approved'
#         }
#         return data
#     def pending_approval_page(self):
#         data = self.pending_approval_data()
#         self.base_page.send_url(self.BASE_URL + data['path'])
#         time.sleep(3)
#         self.execute_js_code()
#
#     def approved_page(self):
#         data = self.approved_data()
#         self.base_page.send_url(self.BASE_URL + data['path'])
#         time.sleep(3)
#         self.execute_js_code()
#
#
#     def perform_process(self):
#         self.pending_approval_page()
#         self.approved_page()
#

from base_page import BasePage
import time
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class ApprovalData:
    """审批相关页面操作"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 审批页面数据
        self.pending_approval_data = {
            'path': '/app/pending-approval'
        }

        self.approved_data = {
            'path': '/app/approved'
        }

    def navigate_to_page(self, path, page_name):
        """导航到指定审批页面"""
        try:
            full_url = self.BASE_URL + path
            self.base_page.send_url(full_url)
            time.sleep(3)
            self.execute_js_code()
            logger.info(f"成功导航到{page_name}页面: {full_url}")
            return True
        except Exception as e:
            logger.error(f"导航到{page_name}页面失败: {e}")
            return False

    def pending_approval_page(self):
        """待审批页面操作"""
        return self.navigate_to_page(
            self.pending_approval_data['path'],
            "待审批"
        )

    def approved_page(self):
        """已审批页面操作"""
        return self.navigate_to_page(
            self.approved_data['path'],
            "已审批"
        )

    def perform_process(self):
        """执行所有审批相关操作"""
        operations = [
            ("待审批页面", self.pending_approval_page),
            ("已审批页面", self.approved_page)
        ]

        for operation_name, operation_func in operations:
            try:
                logger.info(f"开始执行{operation_name}")
                success = operation_func()
                if not success:
                    logger.warning(f"{operation_name}执行失败")
            except Exception as e:
                logger.error(f"{operation_name}执行出错: {e}")


# from base_page import BasePage
# import time
# import js_code
# import url_data
# from logger import get_logger
#
# logger = get_logger()
#
#
# class ApprovalData:
#     """审批相关页面操作"""
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#
#         # 审批页面数据
#         self.pending_approval_data = {
#             'path': '/app/pending-approval'
#         }
#
#         self.approved_data = {
#             'path': '/app/approved'
#         }
#
#     def navigate_to_page(self, path, page_name):
#         """导航到指定审批页面"""
#         try:
#             full_url = self.BASE_URL + path
#             self.base_page.send_url(full_url)
#             time.sleep(3)
#             self.execute_js_code()
#             logger.info(f"成功导航到{page_name}页面: {full_url}")
#             return True
#         except Exception as e:
#             logger.error(f"导航到{page_name}页面失败: {e}")
#             return False
#
#     def pending_approval_page(self):
#         """待审批页面操作"""
#         return self.navigate_to_page(
#             self.pending_approval_data['path'],
#             "待审批"
#         )
#
#     def approved_page(self):
#         """已审批页面操作"""
#         return self.navigate_to_page(
#             self.approved_data['path'],
#             "已审批"
#         )
#
#     def perform_process(self):
#         """执行所有审批相关操作"""
#         operations = [
#             ("待审批页面", self.pending_approval_page),
#             ("已审批页面", self.approved_page)
#         ]
#
#         for operation_name, operation_func in operations:
#             try:
#                 logger.info(f"开始执行{operation_name}")
#                 success = operation_func()
#                 if not success:
#                     logger.warning(f"{operation_name}执行失败")
#             except Exception as e:
#                 logger.error(f"{operation_name}执行出错: {e}")
