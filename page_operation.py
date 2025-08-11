"""
@Functional description ：page operation
@Author  : 周 Ryan
@Email   : ryan.zhou@alloyx.com
@Time    : 2025/8/5 14:57
@ModifyTime    : 2025/8/6 9:20
"""
"""
页面操作模块
"""

from base_page import BasePage
import js_code
import time
from url_data import AlloyxURL

from logger import get_logger
logger = get_logger()


class PageOperation:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.email = 'ryan.zhou@alloyx.com'
        self.password = 'Qwer@1234'
        self.js_code = js_code.send_code()
        self.login_url = AlloyxURL.LOGIN_URL
        self.execute_js_code = lambda: js_code.execute_js_code(self.driver)
        self.email_selector = ['id', 'account']
        self.password_selector = ['xpath', '//*[@id="password"]/span/input']
        self.login_button = ['css', "button[type='submit']"]
    def login(self):
        """执行登录操作"""
        logger.info("开始执行登录操作")
        self.base_page.send_keys(self.email_selector, self.email)
        self.base_page.send_keys(self.password_selector, self.password)
        self.base_page.click(self.login_button)

    def perform_process(self):
        """执行完整流程"""
        try:
            logger.info("开始执行完整流程")
            self.base_page.open()
            self.base_page.send_url(self.login_url)
            logger.info("打开网页成功")
            self.execute_js_code()
            self.login()
            self.execute_js_code()
            logger.info("流程执行完成")
        except Exception as e:
            logger.error(f"执行流程时出错: {e}")
            raise

    def analyze_pages_for_chinese(self, modules=None, page_keys=None):
        """分析页面中的中文元素，返回包含中文元素的URL

        Args:
            modules (list, optional): 要分析的模块列表
            page_keys (list, optional): 要分析的页面键名列表

        Returns:
            dict: 包含中文元素的URL字典，格式为 {url: chinese_elements_info}
        """
        pages_with_chinese = {}
        abandon_url = []
        try:
            # 先执行登录
            self.perform_process()

            # 获取要分析的URL
            if page_keys:
                all_urls = AlloyxURL.get_all_urls()
                urls_to_analyze = {key: all_urls[key] for key in page_keys if key in all_urls}
            elif modules:
                urls_to_analyze = {}
                for module in modules:
                    module_urls = AlloyxURL.get_module_urls(module)
                    urls_to_analyze.update(module_urls)
            else:
                urls_to_analyze = AlloyxURL.get_all_urls()

            # 遍历所有URL并执行分析
            for key, url in urls_to_analyze.items():
                if url == self.login_url:  # 跳过登录页面
                    continue

                logger.info(f"开始分析页面: {key} - {url}")
                try:
                    self.base_page.send_url(url)
                    time.sleep(3)  # 等待页面加载
                    # 修复：正确调用execute_js_code
                    result = self.execute_js_code()

                    # 检查是否有中文元素
                    if result and 'chinese' in result and len(result['chinese']) > 0:
                        pages_with_chinese[url] = {
                            'key': key,
                            'chinese_count': len(result['chinese']),
                            'chinese_elements': result['chinese']
                        }
                        logger.info(f"页面 {key} 包含 {len(result['chinese'])} 个中文元素")
                    else:
                        abandon_url.append(url)
                        logger.info(f"页面 {key} 没有包含中文元素")

                    logger.info(f"页面 {key} 分析完成")

                except Exception as e:
                    logger.error(f"分析页面 {key} 时出错: {e}")
                    continue

        except Exception as e:
            logger.error(f"执行页面分析时出错: {e}")
            raise

        if len(abandon_url) > 0:
            logger.info(f"不含有中文元素的页面有 {len(abandon_url)} 个")
        return pages_with_chinese


    def print_pages_with_chinese(self, pages_with_chinese):
        """打印包含中文元素的页面信息

        Args:
            pages_with_chinese(dict): 包含中文元素的页面字典
        """
        if not pages_with_chinese:
            logger.info("未发现包含中文元素的页面")
            return

        logger.info("\n========== 包含中文元素的页面 ==========")
        for url, info in pages_with_chinese.items():
            logger.info(f"页面键名: {info['key']}")
            logger.info(f"页面URL: {url}")
            logger.info(f"中文元素数量: {info['chinese_count']}")
            logger.info("中文元素详情:")
            # 修复：修正键名 ' chinese_elements' -> 'chinese_elements'
            chinese_elements = info.get('chinese_elements', [])
            for element in chinese_elements[:5]:  # 只显示前5个元素
                logger.info(f"  标签: {element['tag']}, 文本: {element['text']}")
            if info['chinese_count'] > 5:
                logger.info(f"  ... 还有 {info['chinese_count'] - 5} 个元素")
            logger.info("-" * 50)


def main():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    # 配置Chrome选项
    chrome_options = Options()
    # 如果需要无头模式，取消下面的注释
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 初始化浏览器
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        perform = PageOperation(driver)

        # 分析所有页面中的英文元素
        pages_with_english = perform.analyze_pages_for_chinese()

        # 打印结果
        perform.print_pages_with_chinese(pages_with_english)

        # 或者只分析特定模块:
        # pages_with_english = perform.analyze_pages_for_english(modules=['wallet', 'card'])
        # perform.print_pages_with_english(pages_with_english)

        # 或者分析特定页面:
        # pages_with_english = perform.analyze_pages_for_english(page_keys=['wallet', 'card', 'transaction'])
        # perform.print_pages_with_english(pages_with_english)

    except Exception as e:
        logger.error(f"程序执行出错: {e}")
    finally:
        # 确保浏览器被正确关闭
        driver.quit()


if __name__ == '__main__':
    main()
