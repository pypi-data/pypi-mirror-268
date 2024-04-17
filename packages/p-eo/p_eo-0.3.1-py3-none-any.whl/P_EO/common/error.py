class PageEleObject(Exception):
    """
    异常基类
    """

    def __init__(self, err_msg="", desc='', loc='', method='', **kwargs):
        self.msg = err_msg
        self.desc = desc
        self.loc = loc
        self.method = method
        self.kwargs = kwargs

    def __str__(self):
        _msg = self.msg
        _msg += f', describe: {self.desc}' if self.desc else ''
        _msg += f', method: {self.method}' if self.method else ''
        _msg += f', loc: {self.loc}' if self.loc else ''
        for k, v in self.kwargs.items():
            _msg += f', {k}: {v}'
        return _msg


class EleNotFoundError(PageEleObject):
    def __init__(self, desc, loc, method):
        super().__init__(desc=desc, loc=loc, method=method)
        self.msg = '元素未找到'


class EleFindTimeoutError(PageEleObject):
    def __init__(self, desc, loc, method):
        super().__init__(desc=desc, loc=loc, method=method)
        self.msg = '元素查找超时'


class EleNotDisplayedError(PageEleObject):
    def __init__(self, desc, loc, method):
        super().__init__(desc=desc, loc=loc, method=method)
        self.msg = '元素存在但是不可见'


class EleNotEnableError(PageEleObject):
    def __init__(self, desc, loc, method):
        super().__init__(desc=desc, loc=loc, method=method)
        self.msg = '元素存在但是不可交互'


class EleInputError(PageEleObject):
    def __init__(self, desc, loc, method, send_value, tag_value):
        super().__init__(desc=desc, loc=loc, method=method, send_value=send_value, tag_value=tag_value)
        self.msg = '元素输入内容错误'
