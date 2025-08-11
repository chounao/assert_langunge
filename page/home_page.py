#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：home page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/6 13:50
@ModifyTime    : 2025/8/8 15:50
"""
# from base_page import BasePage
# import time
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class HomePage:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#     def home_data(self):
#         data = {
#             'path':'/app/home',
#             'notifications_selector':['class','text-center'],
#             'notifications_view_selector':['class','mt-2'],
#             'button':['tag','button'],
#             'view_button_selector':['class','text-link'],
#             'detall_button_selector':['class','px-3']
#
#         }
#         return data
#
#     def home_page(self):
#         data = self.home_data()
#         new_url = self.BASE_URL + data['path']
#         # self.base_page.send_url(new_url)
#         time.sleep(5)
#         logger.info(f"首页url为：{new_url}")
#         logger.info('点击通知')
#         self.base_page.click(data['notifications_selector'])
#         self.execute_js_code()
#         logger.info("通知pass")
#         try:
#             #通知有些账户数据是空的
#             time.sleep(5)
#             logger.info('点击查看')
#             self.base_page.find_element(data['button'],'View')[0].click()
#             self.execute_js_code()
#             logger.info("查看pass")
#             self.base_page.close_modal_by_esc()
#             logger.info("关闭查看pass")
#         except Exception as e:
#             logger.error(e)
#
#         self.base_page.clicks(data['view_button_selector'],'View')
#         logger.info('点击view')
#         self.execute_js_code()
#         self.base_page.clicks(data['detall_button_selector'], 'Approval process')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("查看按钮pass")
#
#
#     def perform_process(self):
#         self.home_page()


from base_page import BasePage
import time
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class HomePage:
    """首页相关操作"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 首页数据
        self.home_data = {
            'path': '/app/home',
            'notifications_selector': ['class', 'text-center'],
            'notifications_view_selector': ['class', 'mt-2'],
            'button': ['tag', 'button'],
            'view_button_selector': ['class', 'text-link'],
            'detail_button_selector': ['class', 'px-3'],
            'popup_selector': ['class', 'ant-notification-notice-wrapper'],
            'refresh_button_selector': ['class', 'ant-notification-notice-btn']
        }
    def close_popup(self):
        """关闭通知弹窗"""
        try:
            self.base_page.find_elements(self.home_data['popup_selector'])
            logger.info("弹窗存在")
            self.execute_js_code()
            self.base_page.click(self.home_data['refresh_button_selector'])
            time.sleep(5)
            logger.info("关闭弹窗pass")
        except Exception as e:
            logger.error(f"无更新弹窗: {e}")
    def navigate_to_home(self):
        """导航到首页"""
        new_url = self.BASE_URL + self.home_data['path']
        logger.info(f"首页url为：{new_url}")
        # self.base_page.send_url(new_url)
        time.sleep(5)
        return new_url

    def handle_notifications(self):
        """处理通知相关操作"""
        logger.info('点击通知')
        self.base_page.click(self.home_data['notifications_selector'])
        self.execute_js_code()
        logger.info("通知pass")

        try:
            # 通知有些账户数据是空的
            time.sleep(5)
            logger.info('点击查看通知')
            elements = self.base_page.find_element_by_text(self.home_data['button'], 'View')
            if elements is not None:
                elements[0].click()
                self.execute_js_code()
                logger.info("查看pass")
                self.base_page.close_modal_by_esc()
                logger.info("关闭查看pass")
        except Exception as e:
            logger.error(f"没有通知可以查看")

    def process_view_buttons(self):
        """处理查看按钮相关操作"""
        self.base_page.clicks(self.home_data['view_button_selector'], 'View')
        logger.info('点击view')
        self.execute_js_code()

        self.base_page.clicks(self.home_data['detail_button_selector'], 'Approval process')
        self.execute_js_code()
        self.base_page.close_modal_by_esc()
        logger.info("查看按钮pass")

    def perform_process(self):
        """执行首页完整流程"""
        try:
            logger.info("开始执行首页流程")
            self.close_popup()
            self.navigate_to_home()
            self.handle_notifications()
            self.process_view_buttons()
            logger.info("首页流程执行完成")
        except Exception as e:
            logger.error(f"执行首页流程时出错: {e}")
            raise
