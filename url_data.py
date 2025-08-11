#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：url page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/5 09:28
@ModifyTime    : 2025/8/6 9:55
"""
"""
URL数据配置模块
"""
BASE_URL = 'https://test.d1b76915868gf9.amplifyapp.com'
class AlloyxURL:
    """
    Alloyx系统各页面URL配置类
    """

    # def __init__(self):
    #     self.BASE_URL = "https://your-base-url.com"
    # 基础URL

    sign_in='/sign-in'
    # 路径定义字典
    PATHS = {
        # 认证相关

        'sign_up': '/sign-up/',
        'private_policy': '/private-policy/',
        'user_agreement': '/user-agreement/',

        # 首页相关
        'notice_center': '/app/notice-center/',#重定向到app/home
        'home_path': '/app/home/',

        # 钱包模块
        'wallet': '/app/wallet/',
        'recharge': '/app/wallet/recharge/',
        # 'tradego': '/app/wallet/tradego/', #重定向到app/home
        # 'exchange': '/app/wallet/exchange/',#404
        'payee': '/app/payee/',
        'add_payee': '/app/payee/add/',
        #'add_payee_bank':'app/payee/add?type=bank/',
        'payment': '/app/payment/',
        'transaction': '/app/transaction/',

        # 商务卡模块
        'card': '/app/card/',
        'card_detail': '/app/card/detail/',
        'card_swap': '/app/card/swap/',
        'card_account_pay': '/app/card/account-pay/',
        #'card_account_transfer_out': '/app/card/account-transfer-out/', #重定向到app/home
        'card_transaction': '/app/card-transaction/',
        'reap_holders': '/app/card/reap-holders/',
        'reap_holders_detail': '/app/card/reap-holders-detail/',
        'reap_card_create': '/app/card/reap-create-card/',
        'reap_holders_create': '/app/card/reap-holders-create/',

        # 审批模块

        #'i_initiated_approval': '/app/i-initiated-approval/',#重定向到app/home
        'pending_approval': '/app/pending-approval/',
        'approved': '/app/approved/',

        # 管理模块
        'structure_management': '/app/structure-management/',
        'member_management': '/app/member-management/',
        'role_management': '/app/role-management/',
        'risk_setting': '/app/risk-setting/',
        'transfer_out': '/app/transfer-out/',

        # 稳定币模块
        'merchant_management': '/app/checkout/merchant/',
        'add_merchant': '/app/checkout/merchant/add/',
        'merchant_detail': '/app/checkout/merchant/detail/',
        'asset_management': '/app/checkout/asset/',
        'asset_withdraw': '/app/checkout/asset/withdraw/',
    }

    # 模块分组
    MODULES = {
        'auth': [ 'sign_up',  'private_policy', 'user_agreement'],
        'home': [ 'notice_center', 'home_path'],
        'wallet': ['wallet', 'recharge',  'payee', 'add_payee', 'add_payee_bank','payment', 'transaction'],
        'card': ['card', 'card_detail', 'card_swap', 'card_account_pay', 'card_transaction', 'reap_holders', 'reap_holders_detail', 'reap_card_create', 'reap_holders_create'],
        'approval': [  'pending_approval', 'approved'],
        'management': ['structure_management', 'member_management', 'role_management', 'risk_setting', 'transfer_out'],
        'checkout': ['merchant_management', 'add_merchant', 'merchant_detail',
                    'asset_management', 'asset_withdraw',]
    }

    # 生成完整URL字典
    URLS = {key: f'{BASE_URL}{path}' for key, path in PATHS.items()}

    # 单独定义登录URL（主要入口）
    LOGIN_URL = f'{BASE_URL}{sign_in}'

    @classmethod
    def get_all_urls(cls) -> dict:
        """
        获取所有URL配置

        Returns:
            dict: 包含所有URL的字典 {key: full_url}
        """
        return cls.URLS

    @classmethod
    def get_module_urls(cls, module_name: str) -> dict:
        """
        获取指定模块的所有URL

        Args:
            module_name (str): 模块名称

        Returns:
            dict: 指定模块的URL字典
        """
        if module_name not in cls.MODULES:
            return {}

        return {key: cls.URLS[key] for key in cls.MODULES[module_name] if key in cls.URLS}

    @classmethod
    def get_path_by_key(cls, key: str) -> str:
        """
        根据键名获取路径

        Args:
            key (str): 路径键名

        Returns:
            str: 对应的路径
        """
        return cls.PATHS.get(key, '')

    @classmethod
    def get_url_by_key(cls, key: str) -> str:
        """
        根据键名获取完整URL

        Args:
            key (str): URL键名

        Returns:
            str: 对应的完整URL
        """
        return cls.URLS.get(key, '')

    @classmethod
    def get_all_paths(cls) -> dict:
        """
        获取所有路径配置

        Returns:
            dict: 包含所有路径的字典 {key: path}
        """
        return cls.PATHS

    @classmethod
    def get_all_modules(cls) -> dict:
        """
        获取所有模块分组

        Returns:
            dict: 模块分组信息
        """
        return cls.MODULES
if __name__ == '__main__':
    print(AlloyxURL.get_all_urls())