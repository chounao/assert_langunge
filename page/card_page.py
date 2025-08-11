#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：card page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/7 10:48
@ModifyTime    : 2025/8/11 15:10
"""
# from base_page import BasePage
# import time
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class CardPage:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#     def card_data(self):
#         data = {
#             'path':'/app/card',
#             'call_element':['class','ant-spin-nested-loading css-1l11lr2'],#在这个元素上找Recharge Transfer Out Details
#             'call_element_selector':['class','ant-table-cell'],#Cardholder	 Operate
#             'button':['tag','button'],#Recharge Transfer Out Details
#
#
#
#         }
#         return data
#     def account_pay_data(self):
#         data = {
#             'path':'/app/card/account-pay',
#             #'number_selector':['class',"ant-form-item-control-input-content"]
#             'amount_selector':['id','amount'],#充值数量
#             'button': ['tag', 'button']
#         }
#         return data
#     def create_card_data(self):
#         data = {
#             'path':'/app/card/reap-create-card',
#             # 'number_selector':['class','ant-form-item-control-input-content'],
#             # 'name_selector':['id','access_code'],
#             'button_selector':['tag','submit'],#Confirm Creation
#             'button': ['tag', 'button']
#
#         }
#         return data
#     def reap_holders_data(self):
#         data = {
#             'path':'/app/card/reap-holders',
#             'button':['tag','button']# Details Freeze Delete/Return
#         }
#         return data
#     def create_holders_data(self):
#         data = {
#             'path':'/app/card/reap-holders-create',
#             'button_selector':['tag', 'submit'],#Confirm Submission
#             'put_selector':['class','ant-radio-wrapper'],
#             'button': ['tag', 'button']#Return
#         }
#         return data
#     def card_transaction_data(self):
#         data = {
#             'path':'/app/card-transaction',
#             #'button': ['tag', 'button']#Digital Business Card
#             'xpath_selector':['xpath','//*[@id="root"]/div/div/div/main/div/div[1]/button[2]/span'],
#
#         }
#         return data
#
#
#     def card_page(self):
#         data = self.card_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         logger.info(f"卡片页面url为：{new_url}")
#         try:
#             self.base_page.find_sub_element_for_Twotext(data['call_element'], data["button"],'Cardholder','Details')[0].click()
#             time.sleep(5)
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#
#         except Exception as e:
#             logger.error(f"点击Cardholder按钮时出错: {e}")
#
#         try:
#             self.base_page.find_sub_element_for_Twotext(data['call_element'], data["button"],'Operate','Recharge')[0].click()
#             time.sleep(5)
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#         except Exception as e:
#             logger.error(e)
#         try:
#             self.base_page.find_sub_element_for_Twotext(data['call_element'], data["button"],'Operate','Transfer Out')[0].click()
#             time.sleep(5)
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#         except Exception as e:
#             logger.error(e)
#         try:
#             self.base_page.find_sub_element_for_twotext(data['call_element'], data["button"],'Operate','Details')[0].click()
#             time.sleep(5)
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#         except Exception as e:
#             logger.error(e)
#
#
#         #进入充值界面
#         self.base_page.clicks(data["button"],'Recharge')
#         logger.info("点击充值按钮")
#         self.base_page.send_keys(data['amount_selector'],'1000')
#
#         self.execute_js_code()
#         self.base_page.clicks(data['button'],'Return')
#         logger.info("充值页面pass")
#         time.sleep(5)
#         #进入转出
#         # self.base_page.find_element_by_text(data["buttons_selectors"],data["button"],'Transfer Out')
#         # self.base_page.send_keys(data['number_selector'], '1000')
#         # self.execute_js_code()
#         # self.base_page.clicks(data['button'],'Return')
#
#     def account_pay_page(self):
#         data = self.account_pay_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"卡片页面url为：{new_url}")
#         self.base_page.send_keys(data['amount_selector'], '1000')
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Return')
#         logger.info("充值页面pass")
#
#     def create_card_page(self):
#         data = self.create_card_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"创建卡片页面url为：{new_url}")
#         self.base_page.clicks(data['button'], 'Confirm Creation')
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Return')
#         logger.info("创建卡片页面pass")
#
#     def reap_holders_page(self):
#         data = self.reap_holders_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         self.execute_js_code()
#         logger.info(f"卡片页面url为：{new_url}")
#         self.base_page.clicks(data['button'], 'Details')
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Return')
#         time.sleep(3)
#         self.base_page.clicks(data['button'], 'Freeze')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         self.base_page.clicks(data['button'], 'Delete')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#
#
#
#     def create_holders_page(self):
#         data = self.create_holders_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"创建卡片页面url为：{new_url}")
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Confirm Submission')
#         self.execute_js_code()
#         self.base_page.clicks(data['put_selector'],'Non Company Employees')
#         self.execute_js_code()
#         self.base_page.clicks(data['button'], 'Return')
#
#
#     def card_transaction_page(self):
#         data = self.card_transaction_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"卡片交易页面url为：{new_url}")
#         self.execute_js_code()
#         # self.base_page.clicks(data['button'], 'Digital Business Card')
#         self.base_page.click(data['xpath_selector'])
#         self.execute_js_code()
#
#
#     def perform_process(self):
#         self.card_page()
#         self.account_pay_page()
#         self.create_card_page()
#         self.reap_holders_page()
#         self.create_holders_page()
#         self.card_transaction_page()


from base_page import BasePage
import time
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class CardPage:
    """商务卡相关页面操作"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 初始化所有页面数据
        self.card_data = {
            'path': '/app/card',
            'Operate_call_element': ['xpath', '/html/body/div[1]/div/div/div/main/div/div[7]/div/div/div/div/div[2]/table/tbody/tr[2]/td[6]'],
            'number_call_element': ['xpath', '/html/body/div[1]/div/div/div/main/div/div[7]/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]'],
            'button': ['tag', 'button'],
            #'amount_selector': ['tag', 'id'],
            'amount_element': ['xpath', 'ant-form-item-control-input-content'],
             'amount':['class','ant-input css-1l11lr2 ant-input-outlined']
        }

        self.account_pay_data = {
            'path': '/app/card/account-pay',
            'amount_selector': ['tag', 'Transfer amount'],
            'button': ['tag', 'button']
        }

        self.create_card_data = {
            'path': '/app/card/reap-create-card',
            'button_selector': ['tag', 'submit'],
            'button': ['tag', 'button']
        }

        self.reap_holders_data = {
            'path': '/app/card/reap-holders',
            'button': ['tag', 'button']
        }

        self.create_holders_data = {
            'path': '/app/card/reap-holders-create',
            'button_selector': ['tag', 'submit'],
            'put_selector': ['class', 'ant-radio-wrapper'],
            'button': ['tag', 'button']
        }

        self.card_transaction_data = {
            'path': '/app/card-transaction',
            'xpath_selector': ['xpath', '//*[@id="root"]/div/div/div/main/div/div[1]/button[2]/span']
        }

    def navigate_to_page(self, path, page_name):
        """导航到指定页面"""
        new_url = self.BASE_URL + path
        self.base_page.send_url(new_url)
        self.execute_js_code()
        logger.info(f"{page_name}页面url为：{new_url}")
        return new_url

    def perform_click_action(self, selector, action_name):
        """执行点击操作"""
        try:
            self.base_page.click(selector)
            self.execute_js_code()
            logger.info(f"{action_name}操作成功")
            return True
        except Exception as e:
            logger.error(f"{action_name}操作失败: {e}")
            return False

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

    def perform_form_action(self, selector, value, action_name):
        """执行表单输入操作"""
        try:
            self.base_page.send_keys(selector, value)
            self.execute_js_code()
            logger.info(f"{action_name}操作成功")
            return True
        except Exception as e:
            logger.error(f"{action_name}操作失败: {e}")
            return False
    def perform_form_text_click_action(self, parent_selector, child_selector, text, action_name):
        """执行基于文本的表单点击操作后关闭弹窗"""
        try:
            self.base_page.get_ture_sub_element(parent_selector, child_selector, text).click()
            self.execute_js_code()

            logger.info(f"{action_name}操作成功")
            return True
        except Exception as e:
            logger.error(f"{action_name}操作失败: {e}")
            return False

    def card_page(self):
        """商务卡主页操作"""
        self.navigate_to_page(self.card_data['path'], "卡管理")
        # 进入充值界面
        self.perform_text_action(self.card_data["button"], 'Recharge', "点击充值按钮")
        #self.perform_form_action(self.card_data['amount_selector'], '1000', "输入充值金额")
        self.perform_text_action(self.card_data['button'], 'Return', "返回")
        #操作卡详情
        self.perform_form_text_click_action(self.card_data['number_call_element'], self.card_data['button'], 'Details', "点击卡详情")
        self.base_page.close_modal_by_esc()

        # 执行卡片充值操作
        self.perform_form_text_click_action(self.card_data['Operate_call_element'], self.card_data['button'], 'Recharge', "商务卡充值")
        # self.perform_form_action(self.card_data['amount'], '1000', "输入充值金额")
        self.execute_js_code ()
        self.base_page.clicks(self.card_data['button'], 'Return')
        # 执行卡片转出操作
        self.perform_form_text_click_action(self.card_data['Operate_call_element'], self.card_data['button'], 'Transfer Out', "商务卡转出")
        # self.perform_form_action(self.card_data['amount_selector'], '1000', "输入充值金额")
        self.execute_js_code()
        self.base_page.clicks(self.card_data['button'], 'Return')
        # 执行卡片详情操作
        self.perform_form_text_click_action(self.card_data['Operate_call_element'], self.card_data['button'], 'Details', "商务卡详情详情")
        self.perform_text_action(self.card_data['button'], 'Freeze', "冻结弹窗")
        self.base_page.close_modal_by_esc()
        self.perform_text_action(self.card_data['button'], 'Delete', "删除弹窗")
        self.base_page.close_modal_by_esc()
        self.base_page.clicks(self.card_data['button'], 'Return')






    def account_pay_page(self):
        """账户支付页面操作"""
        self.navigate_to_page(self.account_pay_data['path'], "账户支付")
        self.perform_form_action(self.account_pay_data['amount_selector'], '1000', "输入充值金额")
        self.perform_text_action(self.account_pay_data['button'], 'Return', "返回")

    def create_card_page(self):
        """创建卡片页面操作"""
        self.navigate_to_page(self.create_card_data['path'], "创建卡片")
        self.perform_text_action(self.create_card_data['button'], 'Confirm Creation', "确认创建")
        self.perform_text_action(self.create_card_data['button'], 'Return', "返回")

    def reap_holders_page(self):
        """持卡人管理页面操作"""
        self.navigate_to_page(self.reap_holders_data['path'], "持卡人")

        # 执行持卡人操作
        holder_operations = [
            ('Details', '查看详情', 0),
            ('Return', '返回', 3),
            ('Freeze', '冻结', 0),
            ('Delete', '删除', 0)
        ]

        for action_text, action_name, sleep_time in holder_operations:
            self.perform_text_action(self.reap_holders_data['button'], action_text, action_name)
            if action_text == 'Return':
                time.sleep(sleep_time)
            elif action_text in ['Freeze', 'Delete']:
                self.base_page.close_modal_by_esc()

    def create_holders_page(self):
        """创建持卡人页面操作"""
        self.navigate_to_page(self.create_holders_data['path'], "创建持卡人")
        self.perform_text_action(self.create_holders_data['button'], 'Confirm Submission', "确认提交")
        self.perform_text_action(self.create_holders_data['put_selector'], 'Non Company Employees', "选择非公司员工")
        self.perform_text_action(self.create_holders_data['button'], 'Return', "返回")

    def card_transaction_page(self):
        """卡片交易页面操作"""
        self.navigate_to_page(self.card_transaction_data['path'], "卡片交易")
        self.perform_click_action(self.card_transaction_data['xpath_selector'], "点击Digital Business Card")

    def perform_process(self):
        """执行所有商务卡相关操作"""
        operations = [
            ("商务卡主页", self.card_page),
            ("账户支付页面", self.account_pay_page),
            ("创建卡片页面", self.create_card_page),
            ("持卡人页面", self.reap_holders_page),
            ("创建持卡人页面", self.create_holders_page),
            ("卡片交易页面", self.card_transaction_page)
        ]

        for operation_name, operation_func in operations:
            try:
                logger.info(f"开始执行{operation_name}")
                operation_func()
            except Exception as e:
                logger.error(f"{operation_name}执行出错: {e}")
