#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：wallet page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/6 16:03
@ModifyTime    : 2025/8/8 16:27
"""
# import time
#
# from base_page import BasePage
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class WalletPage:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#
#     def wallet_data(self):
#         data = {
#             'path':'/app/wallet'
#         }
#         return data
#     def transfer_out_data(self):
#         data = {
#             'transfer_button':['class', 'ant-btn-icon'],
#             'path':'/app/transfer-out',
#             'number_selector': ['id', 'amount'],
#             'code_selector': ['id', 'access_code'],
#             'button': ['tag', 'button']
#         }
#         return data
#     def recharge_data(self):
#         data = {
#             'path':'/app/wallet/recharge',
#             'input_selector':['class','ant-radio-wrapper'],
#             'button': ['tag', 'button']
#         }
#         return data
#     def payee_data(self):
#         data = {
#             'path':'/app/payee',
#             'bank_selector': ['class', 'px-3'],
#             'button': ['tag', 'button']#Detail
#         }
#         return data
#     def payee_add_data(self):
#         data = {
#             'path':'/app/payee/add',
#             'Account_Label_selector': ['id', 'payee_name'],
#             'Wallet_Address_selector':['id','wallet_address'],
#             'button': ['tag', 'button'],
#             'put_selector':['tag','name'],
#             'input_selector':['class','ant-radio-wrapper'],
#             'clear_selector':['class','ant-input-suffix'],
#             'bank_name_selector':['id','bank_name'],
#             'account_selector':['id','account_no_iban'],
#             'swiftcode_selector':['id','bic_swift'],
#             'number_selector':['id','routing_number1'],
#         }
#         return data
#     def payment_data(self):
#         data = {
#             'path':'/app/payment',
#             'payment_button_selector': ['class', 'ant-tabs-tab-btn'],
#             'clear_selector': ['class', 'ant-input-suffix'],
#             'bank_name_selector': ['id', 'bank_name'],
#             'account_selector': ['id', 'bank_account'],
#             'swiftcode_selector': ['id', 'swift_code'],
#             # 'number_selector': ['id', 'routing_number1'],
#
#         }
#         return data
#     def transaction_data(self):
#         data = {
#             'path':'/app/transaction',
#             'button': ['tag', 'button']
#         }
#         return data
#     def wallet_page(self):
#         data = self.wallet_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         logger.info(f"钱包页面url为：{new_url}")
#
#
#     def transfer_out_page(self):
#         data = self.transfer_out_data()
#         new_url = self.BASE_URL + data['path']
#         # self.base_page.send_url(new_url)
#         self.base_page.click(data['transfer_button'])
#         # self.base_page.refresh_page()
#         logger.info(f"转账页面url为：{new_url}")
#         self.base_page.send_keys(data['number_selector'], '1000')
#         self.base_page.send_keys(data['code_selector'], '1')
#         self.execute_js_code()
#
#         self.base_page.clicks(data['button'], 'Return')
#         logger.info("转账按钮pass")
#         # self.base_page.clicks(data['button'], 'Transfer Out')
#
#     def recharge_page(self):
#         # self.base_page.clicks(data['button'], 'Recharge')
#
#         data = self.recharge_data()
#         new_url = self.BASE_URL + data['path']
#         logger.info(f"充值页面url为：{new_url}")
#         self.base_page.send_url(new_url)
#         # self.base_page.refresh_page()
#         self.execute_js_code()
#         self.base_page.clicks(data['input_selector'], 'On chain recharge')
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Return')
#         logger.info("充值按钮pass")
#
#     def payee_page(self):
#         data = self.payee_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"收款人url为：{new_url}")
#         self.execute_js_code()
#         try:
#             self.base_page.clicks(data['button'], 'Delete')
#             logger.info("删除按钮pass")
#         except:
#             logger.info("删除按钮不存在")
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         time.sleep(10)
#         self.base_page.clicks(data['bank_selector'], 'Receiving Bank Account')
#         self.execute_js_code()
#         try:
#             self.base_page.clicks(data['button'], 'Delete')
#         except:
#             logger.info("删除按钮不存在")
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info(f"收款方页面pass")
#
#     def payee_add_page(self):
#         data = self.payee_add_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"收款方添加url为：{new_url}")
#         self.base_page.send_keys(data['Account_Label_selector'], '1')
#         self.base_page.click(data['clear_selector'])
#         self.base_page.send_keys(data['Wallet_Address_selector'], ' ')
#         self.base_page.click(data['clear_selector'])
#         logger.info("清空pass")
#         self.execute_js_code()
#         logger.info(f"钱包地址添加页面pass")
#         self.base_page.clicks(data['input_selector'],'Bank Account')
#         self.base_page.send_keys(data['bank_name_selector'], '1')
#         self.base_page.click(data['clear_selector'])
#         self.base_page.send_keys(data['account_selector'], '1')
#         self.base_page.send_keys(data['swiftcode_selector'], '1')
#         self.base_page.send_keys(data['number_selector'], '1')
#         self.execute_js_code()
#         logger.info(f"银行地址添加页面pass")
#         self.base_page.clicks(data['button'], 'Return')
#
#     def payment_page(self):
#         data = self.payment_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         logger.info(f"卡片页面url为：{new_url}")
#         self.base_page.clicks(data['payment_button_selector'],'Solomon payment agent')
#
#         self.base_page.send_keys(data['bank_name_selector'], '1')
#         self.base_page.clear(data['bank_name_selector'])
#         self.base_page.send_keys(data['account_selector'], '1')
#         self.base_page.clear(data['account_selector'])
#         self.base_page.send_keys(data['swiftcode_selector'], '1')
#         self.base_page.clear(data['swiftcode_selector'])
#         self.execute_js_code()
#
#     def transaction_page(self):
#         data = self.transaction_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         try:
#             self.base_page.clicks(data['button'], 'Detail')
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#         except Exception as e:
#             logger.error(e)
#         try:
#             self.base_page.clicks(data['button'], 'Cancel')
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#         except Exception as e:
#             logger.error(e)
#         logger.info(f"交易记录页面url为：{new_url}")
#
#
#     def perform_process(self):
#         self.wallet_page()
#         self.transfer_out_page()
#         self.recharge_page()
#         self.payee_page()
#         self.payee_add_page()
#         self.payment_page()
#         self.transaction_page()


import time
from base_page import BasePage
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class WalletPage:
    """钱包相关页面操作"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 初始化所有页面数据
        self.wallet_data = {'path': '/app/wallet'}

        self.transfer_out_data = {
            'transfer_button': ['class', 'ant-btn-icon'],
            'path': '/app/transfer-out',
            'number_selector': ['id', 'amount'],
            'code_selector': ['id', 'access_code'],
            'button': ['tag', 'button']
        }

        self.recharge_data = {
            'path': '/app/wallet/recharge',
            'input_selector': ['class', 'ant-radio-wrapper'],
            'button': ['tag', 'button']
        }

        self.payee_data = {
            'path': '/app/payee',
            'bank_selector': ['class', 'px-3'],
            'button': ['tag', 'button']
        }

        self.payee_add_data = {
            'path': '/app/payee/add',
            'Account_Label_selector': ['id', 'payee_name'],
            'Wallet_Address_selector': ['id', 'wallet_address'],
            'button': ['tag', 'button'],
            'put_selector': ['tag', 'name'],
            'input_selector': ['class', 'ant-radio-wrapper'],
            'clear_selector': ['class', 'ant-input-suffix'],
            'bank_name_selector': ['id', 'bank_name'],
            'account_selector': ['id', 'account_no_iban'],
            'swiftcode_selector': ['id', 'bic_swift'],
            'number_selector': ['id', 'routing_number1'],
        }

        self.payment_data = {
            'path': '/app/payment',
            'payment_button_selector': ['class', 'ant-tabs-tab-btn'],
            'clear_selector': ['class', 'ant-input-suffix'],
            'bank_name_selector': ['id', 'bank_name'],
            'account_selector': ['id', 'bank_account'],
            'swiftcode_selector': ['id', 'swift_code'],
        }

        self.transaction_data = {
            'path': '/app/transaction',
            'button': ['tag', 'button']
        }

    def navigate_to_page(self, path, page_name):
        """导航到指定页面"""
        new_url = self.BASE_URL + path
        self.base_page.send_url(new_url)
        self.execute_js_code()
        logger.info(f"{page_name}页面url为：{new_url}")
        return new_url

    def perform_simple_action(self, selector, action_name):
        """执行简单点击操作"""
        try:
            self.base_page.click(selector)
            self.execute_js_code()
            logger.info(f"{action_name}pass")
            return True
        except Exception as e:
            logger.error(f"{action_name}失败: {e}")
            return False

    def perform_text_action(self, selector, text, action_name):
        """执行基于文本的点击操作"""
        try:
            self.base_page.clicks(selector, text)
            self.execute_js_code()
            logger.info(f"{action_name}pass")
            return True
        except Exception as e:
            logger.error(f"{action_name}失败: {e}")
            return False

    def perform_form_action(self, selector, value, action_name):
        """执行表单输入操作"""
        try:
            self.base_page.send_keys(selector, value)
            self.execute_js_code()
            logger.info(f"{action_name}pass")
            return True
        except Exception as e:
            logger.error(f"{action_name}失败: {e}")
            return False

    def wallet_page(self):
        """钱包主页操作"""
        self.navigate_to_page(self.wallet_data['path'], "钱包")

    def transfer_out_page(self):
        """转账页面操作"""
        self.perform_simple_action(self.transfer_out_data['transfer_button'], "点击转账按钮")
        self.perform_form_action(self.transfer_out_data['number_selector'], '1000', "输入金额")
        self.perform_form_action(self.transfer_out_data['code_selector'], '1', "输入验证码")
        self.perform_text_action(self.transfer_out_data['button'], 'Return', "返回按钮")

    def recharge_page(self):
        """充值页面操作"""
        self.navigate_to_page(self.recharge_data['path'], "充值")
        self.perform_text_action(self.recharge_data['input_selector'], 'On chain recharge', "选择充值方式")
        self.perform_text_action(self.recharge_data['button'], 'Return', "返回按钮")

    def payee_page(self):
        """收款人页面操作"""
        self.navigate_to_page(self.payee_data['path'], "收款人")

        # 尝试删除操作
        try:
            self.base_page.clicks(self.payee_data['button'], 'Delete')
            logger.info("删除按钮pass")
        except:
            logger.info("删除按钮不存在")

        self.base_page.close_modal_by_esc()
        time.sleep(10)

        self.perform_text_action(self.payee_data['bank_selector'], 'Receiving Bank Account', "选择银行账户")
        #操作详情按钮
        self.perform_text_action(self.payee_data['button'], 'Detail', "详情按钮")
        self.execute_js_code()
        # 再次尝试删除操作
        try:#可能没有数据
            self.base_page.clicks(self.payee_data['button'], 'Delete')
            logger.info("删除按钮pass")
        except:
            logger.info("删除按钮不存在")

        self.base_page.close_modal_by_esc()
        logger.info("收款方页面pass")

    def payee_add_page(self):
        """添加收款人页面操作"""
        self.navigate_to_page(self.payee_add_data['path'], "收款方添加")

        # 填写钱包地址信息
        self.perform_form_action(self.payee_add_data['Account_Label_selector'], '1', "输入账户标签")
        self.perform_simple_action(self.payee_add_data['clear_selector'], "清空输入")
        self.perform_form_action(self.payee_add_data['Wallet_Address_selector'], ' ', "输入钱包地址")
        self.perform_simple_action(self.payee_add_data['clear_selector'], "清空输入")
        logger.info("清空pass")

        # 填写银行账户信息
        self.perform_text_action(self.payee_add_data['input_selector'], 'Bank Account', "选择银行账户")
        self.perform_form_action(self.payee_add_data['bank_name_selector'], '1', "输入银行名称")
        self.perform_simple_action(self.payee_add_data['clear_selector'], "清空输入")
        self.perform_form_action(self.payee_add_data['account_selector'], '1', "输入账户号码")
        self.perform_form_action(self.payee_add_data['swiftcode_selector'], '1', "输入SWIFT代码")
        self.perform_form_action(self.payee_add_data['number_selector'], '1', "输入路由号码")

        self.perform_text_action(self.payee_add_data['button'], 'Return', "返回按钮")

    def payment_page(self):
        """支付页面操作"""
        self.navigate_to_page(self.payment_data['path'], "支付")
        self.perform_text_action(self.payment_data['payment_button_selector'], 'Solomon payment agent', "选择支付代理")

        # 填写银行信息并清空
        self.perform_form_action(self.payment_data['bank_name_selector'], '1', "输入银行名称")
        self.base_page.clear(self.payment_data['bank_name_selector'])
        self.perform_form_action(self.payment_data['account_selector'], '1', "输入账户")
        self.base_page.clear(self.payment_data['account_selector'])
        self.perform_form_action(self.payment_data['swiftcode_selector'], '1', "输入SWIFT代码")
        self.base_page.clear(self.payment_data['swiftcode_selector'])

    def transaction_page(self):
        """交易记录页面操作"""
        self.navigate_to_page(self.transaction_data['path'], "交易记录")

        # 尝试查看详情和取消操作
        actions = [
            ('Detail', '查看详情'),
            ('Cancel', '取消操作')
        ]

        for action_text, action_name in actions:
            try:
                self.base_page.clicks(self.transaction_data['button'], action_text)
                self.execute_js_code()
                self.base_page.close_modal_by_esc()
                logger.info(f"{action_name}pass")
            except Exception as e:
                logger.error(f"没有找到{action_name}按钮: {e}")

    def perform_process(self):
        """执行所有钱包相关操作"""
        operations = [
            ("钱包主页", self.wallet_page),
            ("转账页面", self.transfer_out_page),
            ("充值页面", self.recharge_page),
            ("收款人页面", self.payee_page),
            ("添加收款人页面", self.payee_add_page),
            ("支付页面", self.payment_page),
            ("交易记录页面", self.transaction_page)
        ]

        for operation_name, operation_func in operations:
            try:
                logger.info(f"开始执行{operation_name}")
                operation_func()
            except Exception as e:
                logger.error(f"{operation_name}执行出错: {e}")
