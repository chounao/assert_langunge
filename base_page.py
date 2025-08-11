#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：base page
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/05 09:30
@ModifyTime    : 2025/8/8 09:28
"""

import time
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from logger import get_logger
logger = get_logger()

class BasePage:
    BY_MAP = {
        'id': By.ID,
        'name': By.NAME,
        'class': By.CLASS_NAME,
        'tag': By.TAG_NAME,
        'link': By.LINK_TEXT,
        'partial_link': By.PARTIAL_LINK_TEXT,
        'css': By.CSS_SELECTOR,
        'xpath': By.XPATH
    }

    def __init__(self,driver):
        if driver is not None:
            self.driver = driver
        else:
            # 如果没有传入driver，则创建一个新的Chrome实例
            self.driver = webdriver.Chrome()

    def open(self):
        """
        打开浏览器并最大化窗口
        :return: WebDriver实例
        """

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        return self.driver

    def send_url(self, url):
        """
        打开指定URL
        :param url: 要打开的网址
        """

        try:
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.url_contains(url)
            )
        except TimeoutException:
            raise ValueError(f'{url} 页面加载超时')
        except Exception as e:
            raise ValueError(f'{url} 打开地址错误') from e

    def find_element(self, selector, timeout=10, pool_frequency=0.5):
        """
        查找元素并等待其可见
        :param selector: 元组 (by, value) 例如: ('id', 'username')
        :param timeout: 等待超时时间，默认10秒
        :param pool_frequency: 查询间隔时间，默认0.5秒
        :return: WebElement对象
        """
        by, value = selector

        if by not in self.BY_MAP:
            error_msg = f"不支持的定位方式: {by}"

            raise NameError(error_msg)

        try:
            element = WebDriverWait(self.driver, timeout, pool_frequency).until(
                EC.element_to_be_clickable((self.BY_MAP[by], value))
            )

            return element
        except TimeoutException as e:
            error_msg = f"在{timeout}秒内未找到元素: {by}={value}"

            raise TimeoutException(error_msg) from e

    def find_elements(self, selector, timeout=10, pool_frequency=0.5):
        """
        查找多个元素并等待其可见
        :param selector: 元素定位信息 (by, value)
        :param timeout: 超时的总时长，默认10秒
        :param pool_frequency: 循环去查询的间隙时间，默认0.5秒
        :return: WebElement列表
        """
        by, value = selector

        if by not in self.BY_MAP:
            raise NameError(f"不支持的定位方式: {by}")

        try:
            elements = WebDriverWait(self.driver, timeout, pool_frequency).until(
                EC.presence_of_all_elements_located((self.BY_MAP[by], value))
            )
            return elements
        except TimeoutException as e:
            raise TimeoutException(f"在{timeout}秒内未找到元素: {by}={value}") from e
    def click(self, selector, timeout=10, pool_frequency=0.5):
        """
        点击元素
        :param selector: 元素定位信息
        :param timeout: 超时时间
        :param pool_frequency: 查询间隔
        """
        element = self.find_element(selector, timeout, pool_frequency)
        element.click()

    def send_keys(self, selector, text, timeout=10, pool_frequency=0.5):
        """
        输入文本
        :param selector: 元素定位信息
        :param text: 要输入的文本
        :param timeout: 超时
        :param pool_frequency: 查询间隔
        """
        element = self.find_element(selector, timeout, pool_frequency)
        element.send_keys(text)
        time.sleep(2)

    def clear(self, selector, timeout=10, pool_frequency=0.5):
        """
        清空输入框
        :param selector: 元素定位信息
        :param timeout: 超时时间
        :param pool_frequency: 查询间隔
        """
        logger.debug(f"清空元素内容: {selector}")
        element = self.find_element(selector, timeout, pool_frequency)
        element.clear()

    def get_url(self):
        """
        获取当前页面的URL
        :return: 当前页面的URL
        """
        time.sleep(2)
        return self.driver.current_url
    def find_element_by_text(self, selector, text, timeout=10, pool_frequency=0.5):
        """
        根据文本内容查找匹配的元素
        :param selector: 元素定位信息
        :param text: 目标文本
        :param timeout: 超时时间
        :param pool_frequency: 查询间隔
        :return: 匹配的WebElement
        """

        elements = self.find_elements(selector, timeout, pool_frequency)
        for element in elements:
            if element.text == text:
                logger.info(f"成功找到匹配文本'{text}'的元素")
                return element
        logger.error(f"没有找到匹配文本'{text}'的元素")
        raise Exception("没有找到匹配文本的元素")


    def clicks(self, selector,text, timeout=10, pool_frequency=0.5):
        """
        点击元素
        :param selector: 元素定位信息
        :param text: 目标文本
        :param timeout: 超时时间
        :param pool_frequency: 查询间隔
        """
        logger.info(f"点击元素: {selector}")
        element = self.find_element_by_text(selector, text,timeout, pool_frequency)
        element.click()

    def find_sub_elements(self, parent_selector, child_selector, timeout=10, pool_frequency=0.5):
        """
        通过父元素定位子元素

        :param parent_selector: 父元素定位信息 (by, value)
        :param child_selector: 子元素定位信息 (by, value)
        :param timeout: 超时时间，默认10秒
        :param pool_frequency: 查询间隔，默认0.5秒
        :return: WebElement列表
        """
        try:
            # 先找到父元素
            parent_element = self.find_element(parent_selector, timeout, pool_frequency)

            # 从父元素中查找子元素
            by, value = child_selector

            if by not in self.BY_MAP:
                raise NameError(f"不支持的定位方式: {by}")

            # 使用WebDriverWait等待子元素出现
            child_elements = WebDriverWait(parent_element, timeout, pool_frequency).until(
                lambda _: parent_element.find_elements(self.BY_MAP[by], value)
            )

            return child_elements
        except TimeoutException as e:
            raise TimeoutException(f"在父元素中未找到子元素: {child_selector}") from e
        except Exception as e:
            raise Exception(f"查找子元素时发生错误: {e}") from e
    def find_sub_element_for_text(self, parent_selector, child_selector, text,timeout=10, pool_frequency=0.5):
        """
        通过父元素定位子元素

        :param parent_selector: 父元素定位信息 (by, value)
        :param child_selector: 子元素定位信息 (by, value)
        :param timeout: 超时时间，默认10秒
        :param pool_frequency: 查询间隔，默认0.5秒
        :return: WebElement列表
        """
        try:
            # 先找到父元素
            parent_element = self.find_elements(parent_selector, timeout, pool_frequency)
            for element in parent_element:
                if element.text == text:
                    logger.info(f"成功找到匹配文本'{text}'的元素")
                    return element
            # 从父元素中查找子元素
            by, value = child_selector

            if by not in self.BY_MAP:
                raise NameError(f"不支持的定位方式: {by}")

            # 使用WebDriverWait等待子元素出现
            child_elements = WebDriverWait(parent_element, timeout, pool_frequency).until(
                lambda _: element.find_elements(self.BY_MAP[by], value)
            )

            return child_elements
        except TimeoutException as e:
            raise TimeoutException(f"在父元素中未找到子元素: {child_selector}") from e
        except Exception as e:
            raise Exception(f"查找子元素时发生错误: {e}") from e

    def find_sub_element_for_twoText(self, parent_selector, child_selector, father_text, child_text, timeout=10, pool_frequency=0.5):
        """
        通过父元素定位子元素

        :param parent_selector: 父元素定位信息 (by, value)
        :param child_selector: 子元素定位信息 (by, value)
        :param timeout: 超时时间，默认10秒
        :param pool_frequency: 查询间隔，默认0.5秒
        :return: WebElement列表
        """
        try:
            # 先找到父元素
            parent_element = self.find_elements(parent_selector, timeout, pool_frequency)
            for element in parent_element:
                if element.text == father_text:
                    logger.info(f"成功找到匹配文本'{father_text}'的元素")
                    return element
            # 从父元素中查找子元素
            by, value = child_selector

            if by not in self.BY_MAP:
                raise NameError(f"不支持的定位方式: {by}")

            # 使用WebDriverWait等待子元素出现
            child_elements = WebDriverWait(parent_element, timeout, pool_frequency).until(
                lambda _: element.find_elements(self.BY_MAP[by], value)
            )

            for child_element in child_elements:
                if child_element.text == child_text:
                    logger.info(f"成功找到匹配文本'{child_text}'的元素")
                    return child_element
        except TimeoutException as e:
            raise TimeoutException(f"在父元素中未找到子元素: {child_selector}") from e
        except Exception as e:
            raise Exception(f"查找子元素时发生错误: {e}") from e

    def get_ture_sub_element(self, parent_selector, child_selector, text,timeout=10, pool_frequency=0.5):
        """
        根据父元素和子元素的文本内容查找匹配的元素
        :param parent_selector: 父元素定位信息
        :param child_selector: 子元素定位信息
        :param text: 目标文本
        :param timeout: 超时时间
        :param pool_frequency: 查询间隔
        :return: 匹配的WebElement
        """

        elements = self.find_sub_elements(parent_selector, child_selector,timeout, pool_frequency)
        for element in elements:
            if element.text == text:
                logger.info(f"成功找到匹配文本'{text}'的元素")
                return element
        logger.error(f"没有找到匹配文本'{text}'的元素")
        raise Exception("没有找到匹配文本的元素")

    #点击空白区域
    from selenium.webdriver.common.keys import Keys

    def close_modal_by_esc(self):
        """
        通过ESC键关闭弹窗
        """
        try:
            # 发送ESC键事件
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            logger.info("通过ESC键关闭弹窗")
        except Exception as e:
            logger.error(f"通过ESC键关闭弹窗时出错: {e}")

    def click_blank_area(self):
        """
        点击弹窗外部空白区域以关闭弹窗
        """
        # 首先尝试ESC键关闭
        self.close_modal_by_esc()

        # 如果ESC无效，再尝试点击遮罩层
        try:
            # 尝试点击遮罩层
            self.click(['class', 'ant-modal-mask'], timeout=2)
        except:
            try:
                self.click(['class', 'modal-backdrop'], timeout=2)
            except:
                # 最后尝试点击body
                self.click(['xpath', '//body'])
                time.sleep(2)

    def refresh_page(self):
        logger.info('刷新页面')
        self.driver.refresh()
        time.sleep(2)
