#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Functional description ：json_code
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/5 10:17
@ModifyTime    : 2025/8/7 10:03
"""
from logger import get_logger
logger = get_logger()
import time
from base_page import BasePage
def send_code():
    # 定义要执行的JavaScript代码
    js_code = """
    // 获取所有非脚本/样式元素
    const elements = document.querySelectorAll('*:not(script):not(style)');

    const chineseElements = []; // 包含中文的元素
    const englishElements = []; // 包含英文的元素

    // 正则表达式
    const chineseRegex = /[\u4e00-\u9fa5]/; // 匹配中文
    const englishRegex = /[a-zA-Z]/; // 匹配英文

    elements.forEach(elem => {
        const text = elem.textContent.trim();
        if (!text) return;

        // 检查是否包含中文
        if (chineseRegex.test(text)) {
            chineseElements.push({
                tag: elem.tagName,
                text: text,
                xpath: getXPath(elem) // 获取元素的XPath
            });
        }

        // 检查是否包含英文
        if (englishRegex.test(text)) {
            englishElements.push({
                tag: elem.tagName,
                text: text,
                xpath: getXPath(elem)
            });
        }
    });

    // 辅助函数：获取元素的XPath
    function getXPath(element) {
        if (element.tagName === 'HTML') return '/HTML';
        if (element.id) return `//*[@id="${element.id}"]`;

        let xpath = '';
        while (element && element.nodeType === Node.ELEMENT_NODE) {
            let index = 0;
            let sibling = element.previousSibling;
            while (sibling) {
                if (sibling.nodeType === Node.ELEMENT_NODE && sibling.tagName === element.tagName) {
                    index++;
                }
                sibling = sibling.previousSibling;
            }
            const tagName = element.tagName.toLowerCase();
            xpath = `/${tagName}[${index + 1}]${xpath}`;
            element = element.parentNode;
        }
        return xpath;
    }

    // 高亮显示元素（可选）
    chineseElements.forEach(item => {
        const elem = document.evaluate(item.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (elem) elem.style.border = "2px solid red";
    });

    englishElements.forEach(item => {
        const elem = document.evaluate(item.xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        if (elem) elem.style.border = "2px solid blue";
    });

    // 返回处理结果
    return {
        chinese: chineseElements,
        english: englishElements
    };
    """
    return js_code


def execute_js_code(driver):
    """执行JavaScript代码并输出结果"""
    logger.info("执行JavaScript代码分析页面语言元素")

    try:
        result = driver.execute_script(send_code())
        logger.info("JavaScript代码执行成功")
        # 输出结果
        logger.info("===== 查找包含中文的元素ING =====")

        # 优化：先检查结果再处理
        if result and 'chinese' in result:
            chinese_count = len(result['chinese'])
            if chinese_count > 0:
                logger.info(f'中文元素有{chinese_count}个')
                for item in result['chinese']:
                    logger.info(f"标签: {item['tag']}, 文本: {item['text']}, XPath: {item['xpath']}")
            else:
                logger.info('===== 没有找到中文元素 =====')
        else:
            logger.info('===== 没有找到中文元素 =====')

        # 停留一段时间以便观察页面高亮效果
        time.sleep(2)
        return result
    except Exception as e:
        logger.error(f"执行JavaScript代码时出错: {e}")
        return None

