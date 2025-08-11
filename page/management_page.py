#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：management page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/7 16:50
@ModifyTime    : 2025/8/8 16:45
"""
# from base_page import BasePage
#
# import time
# import js_code
# import url_data
# from logger import get_logger
# logger = get_logger()
# # BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
# class ManagementData:
#     """管理系统相关页面元素选择器"""
#     def __init__(self, driver):
#         self.driver = driver
#         self.base_page = BasePage(driver)
#         self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
#         self.BASE_URL = url_data.BASE_URL
#     def department_data(self):
#         """组织架构相关元素"""
#         data =  {
#             'path': '/app/structure-management',
#             'add_department_button': ['class', 'ant-btn-icon'],  # 添加部门按钮
#             'edit_department_button': ['class', 'ant-space-item']  # 编辑部门按钮
#         }
#         return  data
#
#     def user_management_data(self):
#         """用户管理相关元素"""
#         data= {
#             'path': '/app/member-management',
#             'add_user_button': ['class', 'ant-btn-icon'],  # 添加用户按钮
#             'user_row_selector': ['class', 'ant-table-row ant-table-row-level-0'],  # 用户行选择器
#             'user_action_buttons': ['tag', 'button']  # 用户操作按钮（重置密码、修改、删除）
#         }
#         return data
#
#     def role_management_data(self):
#         """角色管理相关元素"""
#         data =  {
#             'path': '/app/role-management',
#             'add_role_button': ['class', 'ant-btn-icon'],  # 添加角色按钮
#             'role_action_buttons': ['class', 'ant-space-item']  # 角色操作按钮（删除、编辑）
#         }
#         return data
#
#
#
#     def risk_control_data(self):
#         """审批设置相关元素"""
#         data= {
#             'path': '/app/risk-setting',
#             'risk_setting_tabs': ['class', 'risk-tab-item '] , # 风控设置标签（审批设置、风控策略设置、白名单、黑名单）
#             'add_rule_button': ['tag', 'button'],  # 新增规则按钮
#             # 'enable_switches': ['class', 'ant-spin-container'],  # 开启开关
#             'add_setting_button': ['class', 'ant-btn-icon'],  # 新增设置按钮
#             'add_white_list_button': ['class', 'ant-btn-icon'],  # 新增白名单按钮
#             'add_black_list_button': ['class', 'ant-btn-icon'] , # 新增黑名单按钮
#             'add_button':['tag','button']
#         }
#         return data
#
#     #读取发送请求并执行点击元素的操作
#     def department_operation(self):
#         """部门操作"""
#         data = self.department_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"部门管理页面url为：{new_url}")
#         time.sleep(15)
#         self.base_page.click(data['add_department_button'])
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("添加按钮pass")
#         try:
#             self.base_page.click(data['edit_department_button'],)
#             self.execute_js_code()
#             self.base_page.close_modal_by_esc()
#             logger.info("编辑按钮pass")
#         except Exception as e:
#             logger.error(e)
#             logger.info("编辑按钮fail")
#
#     def user_management_operation(self):
#         """用户管理操作"""
#         data = self.user_management_data()
#         new_url= self.BASE_URL + data['path']
#         self.base_page.send_url(  new_url)
#         logger.info(f"用户管理页面url为：{new_url}")
#
#         self.base_page.click(data['add_user_button'])
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("添加按钮pass")
#
#         self.base_page.clicks(data['edit_department_button'],'Reset password')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("重置密码按钮pass")
#
#         self.base_page.clicks(data['edit_department_button'],'Edit')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("编辑按钮pass")
#         self.base_page.clicks(data['edit_department_button'],'Delete')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("删除按钮pass")
#
#     def role_management_operation(self):
#         """角色管理操作"""
#         data = self.role_management_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         time.sleep(15)
#         logger.info(f"角色管理页面url为：{new_url}")
#
#         self.base_page.click(data['add_role_button'])
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("添加按钮pass")
#
#         self.base_page.clicks(data['role_action_buttons'],'Delete')
#         time.sleep(5)
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("删除按钮pass")
#
#         self.base_page.clicks(data['role_action_buttons'],'Edit')
#         time.sleep(5)
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("编辑按钮pass")
#
#     def risk_control_operation(self):
#         """风控设置操作"""
#         data = self.risk_control_data()
#         new_url = self.BASE_URL + data['path']
#         self.base_page.send_url(new_url)
#         logger.info(f"风控页面url为：{new_url}")
#
#         # self.base_page.clicks(data['risk_setting_tabs'],'Approval Settings')
#         self.execute_js_code()
#         logger.info("审批设置pass")
#         self.base_page.clicks(data['add_rule_button'],'Add review rules')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("添加审核规则按钮pass")
#         self.base_page.clicks(data['add_button'],'Return')
#
#
#         self.base_page.clicks(data['risk_setting_tabs'],'Risk control strategy setting')
#         self.execute_js_code()
#         logger.info("风控策略设置pass")
#         self.base_page.clicks(data['add_button'],'New strategy')
#         self.execute_js_code()
#         self.base_page.close_modal_by_esc()
#         logger.info("添加风控策略按钮pass")
#
#         self.base_page.clicks(data['risk_setting_tabs'],'White list')
#         self.execute_js_code()
#         logger.info("白名单pass")
#         self.base_page.clicks(data['add_button'], 'Add whitelist')
#         self.base_page.close_modal_by_esc()
#         logger.info("添加白名单按钮pass")
#
#         self.base_page.clicks(data['risk_setting_tabs'],'Black list')
#         print("-----------------")
#         self.execute_js_code()
#         logger.info("黑名单pass")
#         self.base_page.clicks(data['add_button'], 'Add blacklist')
#         self.base_page.close_modal_by_esc()
#         logger.info("添加黑名单按钮pass")
#
#     def perform_process(self):
#         """执行操作"""
#
#         self.department_operation()
#         self.user_management_operation()
#         self.role_management_operation()
#         self.risk_control_operation()


from base_page import BasePage
import time
import js_code
import url_data
from logger import get_logger

logger = get_logger()


class ManagementData:
    """管理系统相关页面元素选择器"""

    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.BASE_URL = url_data.BASE_URL

        # 组织架构相关元素
        self.department_data = {
            'path': '/app/structure-management',
            'add_department_button': ['class', 'ant-btn-icon'],  # 添加部门按钮
            'edit_department_button': ['class', 'ant-space-item']  # 编辑部门按钮
        }

        # 用户管理相关元素
        self.user_management_data = {
            'path': '/app/member-management',
            'add_user_button': ['class', 'ant-btn-icon'],  # 添加用户按钮
            'user_row_selector': ['class', 'ant-table-row ant-table-row-level-0'],  # 用户行选择器
            'user_action_buttons': ['tag', 'button']  # 用户操作按钮（重置密码、修改、删除）
        }

        # 角色管理相关元素
        self.role_management_data = {
            'path': '/app/role-management',
            'add_role_button': ['class', 'ant-btn-icon'],  # 添加角色按钮
            'role_action_buttons': ['tag', 'button']  # 角色操作按钮（删除、编辑）
        }

        # 审批设置相关元素
        self.risk_control_data = {
            'path': '/app/risk-setting',
            'risk_setting_tabs': ['class', 'risk-tab-item '],  # 风控设置标签
            'add_rule_button': ['tag', 'button'],  # 新增规则按钮
            'add_setting_button': ['class', 'ant-btn-icon'],  # 新增设置按钮
            'add_white_list_button': ['class', 'ant-btn-icon'],  # 新增白名单按钮
            'add_black_list_button': ['class', 'ant-btn-icon'],  # 新增黑名单按钮
            'add_button': ['tag', 'button']
        }

    def navigate_to_page(self, path, page_name):
        """导航到指定页面"""
        new_url = self.BASE_URL + path
        self.base_page.send_url(new_url)
        logger.info(f"{page_name}页面url为：{new_url}")
        return new_url

    def perform_operation(self, selector, operation_name):
        """执行通用操作"""
        try:
            self.base_page.click(selector)
            self.execute_js_code()
            self.base_page.close_modal_by_esc()
            logger.info(f"{operation_name}pass")
        except Exception as e:
            logger.error(f"{operation_name}失败: {e}")

    def perform_text_operation(self, selector, text, operation_name):
        """执行基于文本的通用操作"""
        try:
            self.base_page.clicks(selector, text)
            self.execute_js_code()
            self.base_page.close_modal_by_esc()
            logger.info(f"{operation_name}pass")
        except Exception as e:
            logger.error(f"{operation_name}失败: {e}")

    def department_operation(self):
        """部门操作"""
        self.navigate_to_page(self.department_data['path'], "部门管理")
        time.sleep(15)

        self.perform_operation(self.department_data['add_department_button'], "添加按钮")
        self.perform_operation(self.department_data['edit_department_button'], "编辑按钮")

    def user_management_operation(self):
        """用户管理操作"""
        self.navigate_to_page(self.user_management_data['path'], "用户管理")


        self.perform_operation(self.user_management_data['add_user_button'], "添加用户按钮")
        try:
            self.perform_text_operation(self.user_management_data['user_action_buttons'],
                                        'Reset password', "重置密码按钮")
        except Exception as e:
            logger.error(f"没有找到重置密码按钮/root账户没有这个按钮")
        try:
            self.perform_text_operation(self.user_management_data['user_action_buttons'],
                                        'Modify', "编辑按钮")
        except Exception as e:
            logger.error(f"编辑按钮没有找到: {e}")
        try:
            self.perform_text_operation(self.user_management_data['user_action_buttons'],
                                    'Delete', "删除按钮")
        except Exception as e:
            logger.error(f"删除按钮没有摘到/root账户没有这个按钮: {e}")

    def role_management_operation(self):
        """角色管理操作"""
        self.navigate_to_page(self.role_management_data['path'], "角色管理")
        time.sleep(15)

        self.perform_operation(self.role_management_data['add_role_button'], "添加角色按钮")
        self.perform_text_operation(self.role_management_data['role_action_buttons'],
                                    'Delete', "删除角色按钮")
        self.perform_text_operation(self.role_management_data['role_action_buttons'],
                                    'Edit', "编辑角色按钮")

    def risk_control_operation(self):
        """风控设置操作"""
        self.navigate_to_page(self.risk_control_data['path'], "风控")

        # 审批设置
        self.perform_text_operation(self.risk_control_data['add_rule_button'],
                                    'Add review rules', "添加审核规则按钮")
        self.perform_text_operation(self.risk_control_data['add_button'],
                                    'Return', "返回按钮")

        # 风控策略设置
        self.perform_text_operation(self.risk_control_data['risk_setting_tabs'],
                                    'Risk control strategy setting', "风控策略设置")
        self.perform_text_operation(self.risk_control_data['add_button'],
                                    'New strategy', "添加风控策略按钮")

        # 白名单
        self.perform_text_operation(self.risk_control_data['risk_setting_tabs'],
                                    'White list', "白名单")
        self.perform_text_operation(self.risk_control_data['add_button'],
                                    'Add whitelist', "添加白名单按钮")

        # 黑名单
        self.perform_text_operation(self.risk_control_data['risk_setting_tabs'],
                                    'Black list', "黑名单")
        self.perform_text_operation(self.risk_control_data['add_button'],
                                    'Add blacklist', "添加黑名单按钮")

    def perform_process(self):
        """执行所有管理操作"""
        operations = [
            ("部门操作", self.department_operation),
            ("用户管理操作", self.user_management_operation),
            ("角色管理操作", self.role_management_operation),
            ("风控设置操作", self.risk_control_operation)
        ]

        for operation_name, operation_func in operations:
            try:
                logger.info(f"开始执行{operation_name}")
                operation_func()
            except Exception as e:
                logger.error(f"{operation_name}执行出错: {e}")

