import abc
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from P_EO.common.config import Default
from P_EO.common.error import EleFindTimeoutError, EleNotDisplayedError, EleNotEnableError, EleInputError, \
    EleNotFoundError
from P_EO.common.log import peo_logger
from P_EO.core.javascript import JavaScript


class Action(metaclass=abc.ABCMeta):
    def __init__(self):
        self._driver: WebDriver = None
        self._desc = ''
        self._loc = ''
        self._method: By = None

    def __get__(self, instance, owner):
        if self._driver is None:
            self._driver = instance.driver
        return self

    @abc.abstractmethod
    def ele(self) -> WebElement:
        """
        返回一个 WebElement 对象
        :return:
        """
        raise NotImplementedError('该方法需要重写')

    @property
    def driver(self):
        """
        返回当前的 WebDriver 对象
        :return:
        """
        return self._driver

    @property
    def describe(self) -> str:
        """
        返回当前元素的描述
        :return:
        """
        return self._desc

    @property
    def loc(self) -> str:
        """
        返回当前元素的定位写法
        :return:
        """
        return self._loc

    @loc.setter
    def loc(self, value):
        """
        给当前元素的定位重新赋值
        :param value:
        :return:
        """
        self._loc = value

    def loc_replace(self, **kwargs):
        """
        替换 loc 中指定字符串
        :param kwargs:
        :return:
        """
        for key, value in kwargs.items():
            self.loc = self.loc.replace(key, value)
        return self

    @property
    def method(self) -> By:
        """
        返回当前元素的定位方法
        :return:
        """
        return self._method

    def click(self, wait=Default.ACTION_WAIT, check_displayed=True, check_enabled=True):
        """
        元素点击
        :param wait:
        :param check_displayed:
        :param check_enabled:
        :return:
        """
        if check_displayed and not self.displayed:
            peo_logger().error(
                f'当前元素存在但不可见 describe: {self.describe}, method: {self.method}, loc: {self.loc}')
            raise EleNotDisplayedError(desc=self.describe, loc=self.loc, method=self.method)

        self.scrolled_into_view()
        if check_enabled and not self.enabled:
            peo_logger().error(
                f'当前元素存在但不可交互 describe: {self.describe}, method: {self.method}, loc: {self.loc}')
            raise EleNotEnableError(desc=self.describe, loc=self.loc, method=self.method)

        self.ele().click()
        peo_logger().info(f'元素 {self.describe} 点击成功')
        time.sleep(wait)

    def action_chains(self, wait=Default.ACTION_WAIT):
        """
        元素滚动到可见，并返回一个ActionChains对象
        :param wait:
        :return:
        """
        self.scrolled_into_view()
        # ActionChains(self.driver).scroll_to_element(self.ele()).perform()  # selenium==3.141.0 好像没有这个语法，>=4以上好像才有
        time.sleep(wait)
        return ActionChains(self.driver)

    def click_by_action_chains(self, wait=Default.ACTION_WAIT):
        """
        元素滚动并点击
        :param wait:
        :return:
        """
        self.action_chains(wait).click(self.ele()).perform()
        peo_logger().info(f'元素 {self.describe} 点击(ActionChains)成功')
        time.sleep(wait)

    def double_click(self, wait=Default.ACTION_WAIT):
        """
        元素滚动并双击
        :param wait:
        :return:
        """
        self.action_chains(wait).double_click(self.ele()).perform()
        peo_logger().info(f'元素 {self.describe} 双击(ActionChains)成功')
        time.sleep(wait)

    def right_click(self, wait=Default.ACTION_WAIT):
        """
        元素滚动并右键
        :param wait:
        :return:
        """
        self.action_chains(wait).context_click(self.ele()).perform()
        peo_logger().info(f'元素 {self.describe} 右键(ActionChains)成功')
        time.sleep(wait)

    def drag_to_pos(self, x, y, wait=Default.ACTION_WAIT):
        """
        拖拽到指定坐标
        :param x:
        :param y:
        :param wait:
        :return:
        """
        self.action_chains(wait).drag_and_drop_by_offset(self.ele(), xoffset=x, yoffset=y).perform()
        peo_logger().info(f'元素 {self.describe} 拖拽(ActionChains)至 {x}, {y} 成功')
        time.sleep(wait)

    def drag_to_ele(self, ele, wait=Default.ACTION_WAIT):
        """
        拖拽到指定元素上
        :param ele:
        :param wait:
        :return:
        """
        from P_EO import Element
        if isinstance(ele, Element):
            ele = ele.ele()

        if not isinstance(ele, WebElement):
            raise TypeError('ele 参数类型错误，必须是 WebElement 类型')

        self.action_chains(wait).drag_and_drop(source=self.ele(), target=ele).perform()
        peo_logger().info(f'元素 {self.describe} 拖拽(ActionChains)至元素 {ele} 成功')
        time.sleep(wait)

    def hover(self, wait=Default.ACTION_WAIT):
        """
        悬停
        :param wait:
        :return:
        """
        self.action_chains(wait).move_to_element(self.ele()).perform()
        peo_logger().info(f'元素 {self.describe} 悬停(ActionChains)成功')
        time.sleep(wait)

    def clear(self, force_clear=False):
        """
        清理输入内容
        :param force_clear:
        :return:
        """
        _ele = self.ele()
        _ele.clear()
        if force_clear:
            JavaScript(driver=self.driver).clear_input_control(_ele)
        peo_logger().info(f'元素 {self.describe} 清理输入成功')

    def send_keys(self, *values):
        """
        输入内容
        :param values:
        :return:
        """
        self.ele().send_keys(*values)
        _values = ''
        for i in values:
            _values += str(i)
        peo_logger().info(f'元素 {self.describe} 键入内容 {_values}')

    def send_keys_by_str(self, value, wait=Default.ACTION_WAIT, clear=False, force_clear=False):
        """
        输入字符串内容
        :param value:
        :param wait:
        :param clear:
        :param force_clear:
        :return:
        """
        if not isinstance(value, str):
            value = str(value)

        self.scrolled_into_view()
        if clear:
            self.clear(force_clear)

        self.ele().send_keys(value)
        tag = self.ele().get_attribute('value')
        if tag != value:
            peo_logger().error(
                f'当前输入内容不正确 describe: {self.describe}, method: {self.method}, loc: {self.loc}, expect: {value}, target: {tag}')
            raise EleInputError(desc=self.describe, loc=self.loc, method=self.method, send_value=value, tag_value=tag)
        peo_logger().info(f'元素 {self.describe} 输入内容成功 {value}')
        time.sleep(wait)

    @property
    def text(self):
        """
        返回与元素文本
        :return:
        """
        return self.ele().text.strip()

    def get_attribute(self, attribute):
        """
        返回元素属性
        :param attribute:
        :return:
        """
        return self.ele().get_attribute(attribute).strip()

    def wait(self, timeout=Default.TIMEOUT, interval=Default.INTERVAL):
        """
        等待元素出现并操作
        :param timeout:
        :param interval:
        :return:
        """
        if self.wait_exists(timeout=timeout, interval=interval):
            peo_logger().info(f'元素 {self.describe} 等待完成')
            return self
        peo_logger().error(f'当前元素查找超时 describe: {self.describe}, method: {self.method}, loc: {self.loc}')
        raise EleFindTimeoutError(desc=self.describe, loc=self.loc, method=self.method)

    def wait_exists(self, timeout=Default.TIMEOUT, interval=Default.INTERVAL):
        """
        轮询判断元素是否存在
        :param timeout:
        :param interval:
        :return:
        """
        start = time.time()
        while time.time() - start <= timeout:
            try:
                res = self.displayed is True
                if res:
                    peo_logger().info(f'元素 {self.describe} 确认存在')
                    return True
            except EleNotFoundError:
                pass
            time.sleep(interval)
        peo_logger().warning(f'元素 {self.describe} 确认不存在')
        return False

    def wait_disappear(self, timeout=Default.TIMEOUT, interval=Default.INTERVAL):
        """
        轮询判断元素是否消失
        :param timeout:
        :param interval:
        :return:
        """
        start = time.time()
        while time.time() - start <= timeout:
            try:
                res = self.displayed is False
                if res:
                    break
            except EleNotFoundError:
                break
            time.sleep(interval)
        else:
            peo_logger().warning(f'元素 {self.describe} 确认未消失')
            return False
        peo_logger().info(f'元素 {self.describe} 确认消失')
        return True

    @property
    def displayed(self):
        """
        判断元素是否可见
        :return:
        """
        return self.ele().is_displayed()

    @property
    def selected(self):
        """
        判断元素是否已选中
        :return:
        """
        return self.ele().is_selected()

    @property
    def enabled(self):
        """
        判断元素是否可交互
        :return:
        """
        return self.ele().is_enabled()

    def scrolled_into_view(self):
        """
        滚动元素到当前视图
        :return: {'x': x, 'y': y}
        """
        return self.ele().location_once_scrolled_into_view

    def save_screenshot(self, file_name):
        """
        保存当前元素为图片
        :param file_name:
        :return:
        """
        self.ele().screenshot(file_name)
        peo_logger().info(f'元素 {self.describe} 保存成功 {file_name}')
        return file_name
