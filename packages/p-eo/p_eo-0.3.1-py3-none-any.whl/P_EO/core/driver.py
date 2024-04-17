import os.path
import time

from selenium.webdriver.remote.webdriver import WebDriver

from P_EO.common.config import Default
from P_EO.common.log import peo_logger
from P_EO.core.javascript import JavaScript


class Driver:
    def __init__(self, driver: WebDriver):
        self.__d = driver
        self.__timeout = None

    @property
    def driver(self):
        """
        返回driver对象
        :return:
        """
        return self.__d

    def set_implicitly_wait(self, timeout: int = None):
        """
        设置隐式等待时间
        :param timeout:
        :return:
        """
        self.__timeout = timeout if timeout else Default.IMPLICITLY_WAIT
        self.__d.implicitly_wait(time_to_wait=self.__timeout)
        peo_logger().debug(f'隐式等待设定: {self.__timeout} s')

    @property
    def get_implicitly_wait(self):
        """
        获取当前隐式等待设定时间
        """
        return self.__timeout if self.__timeout else Default.IMPLICITLY_WAIT

    @property
    def get_cur_window_size(self):
        """
        获取当前网页窗口大小
        :return:
        """
        return self.__d.get_window_size()

    def set_cur_window_size(self, width=0, height=0):
        """
        设定当前窗口大小，如果窗口大小为0，则默认最大化打开
        :param width:
        :param height:
        :return:
        """
        if width > 0 and height > 0:
            self.__d.set_window_size(width=width, height=height)
            peo_logger().debug(f'设定浏览器窗口: {width} {height}')
        else:
            self.__d.maximize_window()
            peo_logger().debug('浏览器窗口最大化')

    @property
    def get_cur_url(self):
        """
        获取当前url
        :return:
        """
        return self.__d.current_url

    def open_url(self, url):
        """
        打开新url
        :param url:
        :return:
        """
        self.__d.get(url)
        peo_logger().debug(f'访问url: {url}')

    @property
    def get_cur_handle(self):
        """
        获取当前窗口handle
        :return:
        """
        return self.__d.current_window_handle

    def switch_frame_to_default(self):
        """
        切换到最外层 frame
        :return:
        """
        self.driver.switch_to.default_content()

    @property
    def get_window_handles(self):
        """
        获取当前所有窗口windows handle
        :return:
        """
        return self.__d.window_handles

    def switch_window(self, handle):
        """
        切换到指定windows handle
        :param handle:
        :return:
        """
        self.__d.switch_to.window(handle)
        peo_logger().debug(f'切换到指定浏览器handle: {handle}')

    def switch_window_by_index(self, index: int):
        """
        根据索引切换windows handle
        :param index: 0, 1, 2,...
        :return:
        """
        _handle = self.get_window_handles[index]
        self.switch_window(_handle)
        peo_logger().debug(f'切换到指定索引handle: {index} - {_handle}')

    def switch_new_window(self):
        """
        切换到最后一个window handle
        :return:
        """
        self.switch_window_by_index(-1)
        peo_logger().debug(f'切换到末尾handle')

    def open_new_window(self, url=''):
        """
        打开一个新tab，如果url有值，则打开指定url
        :param url:
        :return:
        """
        JavaScript(driver=self.__d).open_new_tab(url)
        peo_logger().debug(f'浏览器打开新tab: {url}')

    def goto_new_route(self, route=''):
        """
        切换到同host下新route
        :param route:
        :return:
        """
        JavaScript(driver=self.__d).goto_new_route(route)
        peo_logger().debug(f'浏览器切换路由: {route}')

    @property
    def title(self):
        """
        获取title
        :return:
        """
        return self.__d.title

    def back(self):
        """
        返回
        :return:
        """
        self.__d.back()

    def refresh(self, wait=Default.REFRESH_WAIT):
        """
        刷新
        :param wait: 默认刷新后暂停1s
        :return:
        """
        self.__d.refresh()
        time.sleep(wait)

    def screenshots(self, file_path):
        """
        截图
        :param file_path: 截图完整路径
        :return:
        """
        dir_path = os.path.dirname(file_path)
        if not os.path.exists(dir_path):
            raise FileNotFoundError(f'dir path not found: {dir_path}')
        self.__d.save_screenshot(filename=file_path)
        peo_logger().debug(f'浏览器截图: {file_path}')

    def close(self):
        """
        关闭tab
        :return:
        """
        self.__d.close()
        peo_logger().debug('关闭当前浏览器tab')

    def close_alone(self):
        """
        如果当前tab list不唯一，则可以关闭
        :return:
        """
        if len(self.get_window_handles) > 1:
            self.close()

    def quit(self):
        """
        退出浏览器
        :return:
        """
        self.__d.quit()
        peo_logger().debug('关闭浏览器')

    @property
    def alert(self):
        """
        切换到 Alert 窗口
        :return:
        """
        return self.driver.switch_to.alert
