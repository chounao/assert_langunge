#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：carryout
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/05 11:08
@ModifyTime    : 2025/8/7 11:28
"""
import time
from logger import get_logger
from page import management_page, login_page, checkout_page, approval_page, home_page, wallet_page, card_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.options import Options

logger = get_logger()


def execute_page_process(driver, page_class, page_name):
    """
    统一执行页面流程的函数
    :param driver: WebDriver实例
    :param page_class: 页面类
    :param page_name: 页面名称（用于日志）
    """
    try:
        logger.info(f"开始执行{page_name}")
        perform = page_class(driver)
        perform.perform_process()
        return True
    except Exception as e:
        logger.error(f"{page_name}执行出错: {e}")
        return False


def main():
    # 配置Chrome选项
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = None
    try:
        # 初始化ChromeDriver
        driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager(
                    cache_manager=DriverCacheManager()
                ).install()
            ),
            options=chrome_options
        )

        # 定义要执行的页面流程（取消注释需要执行的页面）
        page_processes = [
            (login_page.LoginPage, "登录"),
            (home_page.HomePage, "首页"),
            (wallet_page.WalletPage, "钱包"),
            (card_page.CardPage, "商务卡"),
            (approval_page.ApprovalData, "审批"),
            (checkout_page.ChenkoutData, "稳定币收款"),
            (management_page.ManagementData, "管理"),
        ]

        # 依次执行各个页面流程
        for page_class, page_name in page_processes:
            if not execute_page_process(driver, page_class, page_name):
                logger.warning(f"{page_name}执行失败，继续执行下一个流程")

    except Exception as e:
        logger.error(f"ChromeDriver初始化失败: {e}")
    finally:
        # 确保浏览器被正确关闭
        if driver:
            driver.quit()


if __name__ == '__main__':
    main()
