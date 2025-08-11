#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：checkout page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/7 14:06
@ModifyTime    : 2025/8/8 17:15
"""
# from base_page import BasePage
# import time
# import js_code
# import url_data
#
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class ChenkoutData:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#
#     def asset_management(self):
#         # 资产管理
#         data = {
#             'path': '/app/checkout/asset',
#         }
#         return data
#
#     def asset_withdraw(self):
#         # 资产提现
#         data = {
#             'path': '/app/checkout/asset/withdraw',
#         }
#         return data
#
#     def checkout_merchant(self):
#         # 提现商户
#         data = {
#             'path': '/app/checkout/merchant',
#             'button':['tag','button'],#Details /Delete /详情（Delete /Add A New Payment Address）
#
#         }
#         return data
#     def add_checkout_merchant(self):
#         # 添加提现商户
#         data = {
#             'path': '/app/checkout/merchant/add',
#         }
#         return data
#     def checkout_order(self):
#         # 提现订单
#         data = {
#             'path': '/app/checkout/order',
#             'button':['tag','button'],#Refund
#         }
#         return data
#     def checkout_order_detail(self):
#         # 提现订单详情
#         data = {
#             'path': '/app/checkout/order/detail',
#         }
#         return data
#     def asset_management_page(self):
#         data = self.asset_management()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#
#     def asset_withdraw_page(self):
#         data = self.asset_withdraw()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#     def checkout_merchant_page(self):
#         data = self.checkout_merchant()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         self.base_page.clicks(data['button'],'Delete')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         self.base_page.clicks(data['button'],'Details')
#         time.sleep(3)
#         self.execute_js_code()
#         self.base_page.clicks(data['button'],'Add A New Payment Address')
#         self.base_page.clicks(data['button'],'Confirm')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         self.base_page.clicks(data['button'], 'Delete')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#     def add_checkout_merchant_page(self):
#         data = self.add_checkout_merchant()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#
#     def checkout_order_page(self):
#         data = self.checkout_order()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         self.base_page.clicks(data['button'],'Refund')
#         self.base_page.close_modal_by_esc()
#
#     def perform_process(self):
#         self.asset_management_page()
#         self.asset_withdraw_page()
#         self.checkout_merchant_page()
#         self.add_checkout_merchant_page()
#         self.checkout_order_page()


from base_page import BasePage
import time
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class ChenkoutData:
    """结算相关页面操作"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 初始化所有页面数据
        self.asset_management_data = {
            'path': '/app/checkout/asset',
        }

        self.asset_withdraw_data = {
            'path': '/app/checkout/asset/withdraw',
        }

        self.checkout_merchant_data = {
            'path': '/app/checkout/merchant',
            'button': ['tag', 'button'],  # Details /Delete /详情（Delete /Add A New Payment Address）
        }

        self.add_checkout_merchant_data = {
            'path': '/app/checkout/merchant/add',
        }

        self.checkout_order_data = {
            'path': '/app/checkout/order',
            'button': ['tag', 'button'],  # Refund
        }

        self.checkout_order_detail_data = {
            'path': '/app/checkout/order/detail',
        }

    def navigate_to_page(self, path, page_name):
        """导航到指定页面"""
        new_url = self.BASE_URL + path
        self.base_page.send_url(new_url)
        self.execute_js_code()
        logger.info(f"导航到{page_name}页面: {new_url}")
        return new_url

    def perform_text_action(self, selector, text, action_name):
        """执行基于文本的点击操作"""
        try:
            self.base_page.clicks(selector, text)
            self.execute_js_code()
            logger.info(f"{action_name}操作成功")
            return True
        except Exception as e:
            logger.error(f"{action_name}操作失败: {e}")
            return False

    def asset_management_page(self):
        """资产管理页面操作"""
        self.navigate_to_page(self.asset_management_data['path'], "资产管理")

    def asset_withdraw_page(self):
        """资产提现页面操作"""
        self.navigate_to_page(self.asset_withdraw_data['path'], "资产提现")

    def checkout_merchant_page(self):
        """提现商户页面操作"""
        self.navigate_to_page(self.checkout_merchant_data['path'], "提现商户")

        # 执行一系列商户操作
        operations = [
            ('Delete', '删除商户'),
            ('Details', '查看详情'),
            ('Add A New Payment Address', '添加新支付地址'),
            ('Confirm', '确认操作'),
            ('Delete', '再次删除')
        ]

        for action_text, action_name in operations:
            self.perform_text_action(self.checkout_merchant_data['button'], action_text, action_name)
            if action_name in ['删除商户', '确认操作', '再次删除']:
                self.base_page.close_modal_by_esc()
            elif action_name == '查看详情':
                time.sleep(3)

    def add_checkout_merchant_page(self):
        """添加提现商户页面操作"""
        self.navigate_to_page(self.add_checkout_merchant_data['path'], "添加提现商户")

    def checkout_order_page(self):
        """提现订单页面操作"""
        self.navigate_to_page(self.checkout_order_data['path'], "提现订单")
        try:
            self.perform_text_action(self.checkout_order_data['button'], 'Refund', "退款操作")
            self.base_page.close_modal_by_esc()
            logger.info("退款操作成功")
        except:
            logger.error("没有找到退款按钮")

    def perform_process(self):
        """执行所有结算相关操作"""
        operations = [
            ("资产管理页面", self.asset_management_page),
            ("资产提现页面", self.asset_withdraw_page),
            ("提现商户页面", self.checkout_merchant_page),
            ("添加提现商户页面", self.add_checkout_merchant_page),
            ("提现订单页面", self.checkout_order_page)
        ]

        for operation_name, operation_func in operations:
            try:
                logger.info(f"开始执行{operation_name}")
                operation_func()
            except Exception as e:
                logger.error(f"{operation_name}执行出错: {e}")

