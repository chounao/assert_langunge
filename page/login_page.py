#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：login page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/6 10:05
@ModifyTime    : 2023/8/8 15:35
"""

"""
# """
# 页面操作模块
# """
#
# from base_page import BasePage
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
#
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#     def login_data(self):
#         data = {
#             'path': '/sign-in',
#             'email_selector': ['id', 'account'],
#             'password_selector': ['xpath', '//*[@id="password"]/span/input'],
#             'login_button': ['css', "button[type='submit']"],
#             'email': 'ryan.zhou@alloyx.com',
#             'password': 'Qwer@1234'
#         }
#         return data
#     def get_login_url(self):
#         """获取完整的登录页面URL"""
#         return f"{self.BASE_URL}{self.login_data['path']}"
#
#     def not_send_email(self):
#         """发送空邮箱"""
#         data = self.login_data()
#         # self.base_page.send_keys(data['email_selector'], '')
#         self.base_page.send_keys(data['password_selector'], data['password'])
#         self.base_page.click(data['login_button'])
#         self.execute_js_code()
#     def not_send_password(self):
#         """发送空密码"""
#         data = self.login_data()
#         self.base_page.clear(data['password_selector'])
#         self.base_page.clear(data['email_selector'])
#         self.base_page.send_keys(data['email_selector'], data['email'])
#         # self.base_page.send_keys(data['password_selector'], '')
#         self.base_page.click(data['login_button'])
#         self.execute_js_code()
#         self.base_page.clear(data['password_selector'])
#         self.base_page.clear(data['email_selector'])
#     def not_send_data(self):
#         data = self.login_data()
#         self.base_page.click(data['login_button'])
#         self.execute_js_code()
#     def login(self):
#         """执行登录操作"""
#         logger.info("开始执行登录操作")
#         data = self.login_data()
#         self.base_page.send_keys(data['email_selector'], data['email'])
#         self.base_page.send_keys(data['password_selector'], data['password'])
#         self.base_page.click(data['login_button'])
#         self.execute_js_code()
#
#     def perform_process(self):
#         """执行完整流程"""
#         data = self.login_data()
#         url = self.BASE_URL+data['path']
#         try:
#             logger.info("开始执行完整流程")
#             self.base_page.open()
#             self.base_page.send_url(url)
#             logger.info("打开网页成功")
#
#             # self.not_send_data()
#
#             self.login()
#
#             logger.info("流程执行完成")
#         except Exception as e:
#             logger.error(f"执行流程时出错: {e}")
#             raise


from base_page import BasePage
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class LoginPage:
    """登录页面操作类"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 登录页面数据
        self.login_data = {
            'path': '/sign-in',
            'email_selector': ['id', 'account'],
            'password_selector': ['xpath', '//*[@id="password"]/span/input'],
            'login_button': ['css', "button[type='submit']"],
            'email': 'ryan.zhou@alloyx.com',
            'password': 'Qwer@1234'
        }

    def get_login_url(self):
        """获取完整的登录页面URL"""
        return f"{self.BASE_URL}{self.login_data['path']}"

    def perform_login_action(self, email='', password=''):
        """执行登录操作"""
        try:
            self.base_page.send_keys(self.login_data['email_selector'], email)
            self.base_page.send_keys(self.login_data['password_selector'], password)
            self.base_page.click(self.login_data['login_button'])
            self.execute_js_code()
            logger.info("登录操作执行完成")
            return True
        except Exception as e:
            logger.error(f"登录操作失败: {e}")
            return False

    def login_with_valid_credentials(self):
        """使用有效凭据登录"""
        logger.info("开始执行登录操作")
        return self.perform_login_action(
            self.login_data['email'],
            self.login_data['password']
        )

    def login_with_empty_fields(self):
        """使用空字段登录（用于测试）"""
        logger.info("执行空字段登录测试")
        return self.perform_login_action('', '')

    def login_with_empty_email(self):
        """使用空邮箱登录（用于测试）"""
        logger.info("执行空邮箱登录测试")
        return self.perform_login_action('', self.login_data['password'])

    def login_with_empty_password(self):
        """使用空密码登录（用于测试）"""
        logger.info("执行空密码登录测试")
        return self.perform_login_action(self.login_data['email'], '')

    def perform_process(self):
        """执行完整流程"""
        url = self.get_login_url()

        try:
            logger.info("开始执行完整流程")
            self.base_page.open()
            self.base_page.send_url(url)
            logger.info("打开网页成功")

            # 可以选择执行不同的登录测试
            # self.login_with_empty_fields()
            # self.login_with_empty_email()
            # self.login_with_empty_password()

            self.login_with_valid_credentials()
            logger.info("流程执行完成")

        except Exception as e:
            logger.error(f"执行流程时出错: {e}")
            raise

