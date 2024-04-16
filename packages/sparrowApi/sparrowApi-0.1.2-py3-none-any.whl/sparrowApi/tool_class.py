import json
import os


class _ToolClass(object):
    """
    工具类
    """
    def __init__(self):
        pass

    @staticmethod
    def return_html(file_name, code='utf-8'):
        """
        返回HTML的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "html"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = f.read()
        return data

    @staticmethod
    def return_xml(file_name, code='utf-8'):
        """
        返回XML的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "xml"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = f.read()
        return data

    @staticmethod
    def return_json(file_name, code='utf-8'):
        """
        返回JSON的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "json"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = json.load(f)
        return data

    @staticmethod
    def return_text(file_name, code='utf-8'):
        """
        返回文本文件的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "other"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = f.read()
        return data

    @staticmethod
    def return_css(file_name, code='utf-8'):
        """
        返回CSS的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "css"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = f.read()
        return data

    @staticmethod
    def return_javascript(file_name, code='utf-8'):
        """
        返回JavaScript的内容
        :param code: 读取文件编码，默认UTF-8
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "javascript"), file_name)
        with open(path, 'r', encoding=code) as f:
            data = f.read()
        return data

    @staticmethod
    def return_image(file_name):
        """
        返回image的内容
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "image"), file_name)
        with open(path, 'rb') as f:
            data = f.read()
        return data

    @staticmethod
    def return_video(file_name):
        """
        返回video的内容
        :param file_name: 文件名
        :return:
        """
        path = os.path.join(os.path.join("static", "video"), file_name)
        with open(path, 'rb') as f:
            data = f.read()
        return data


def return_html(file_name, code='utf-8'):
    """
    返回HTML数据，默认在根目录/static/html/目录下
    :param code: 读取文件编码，默认UTF-8
    :param file_name: 文件名
    :return:
    """
    return _ToolClass.return_html(file_name, code)


def return_javascript(file_name, code='utf-8'):
    """
    返回XML数据，默认在根目录/static/xml/目录下
    :param file_name: 文件名
    :param code: 读取文件编码，默认UTF-8
    :return:
    """
    return _ToolClass.return_javascript(file_name, code)


def return_json(file_name, code='utf-8'):
    """
    返回JSON数据，默认在根目录/static/json/目录下
    :param file_name: 文件名
    :param code: 读取文件编码，默认UTF-8
    :return:
    """
    return _ToolClass.return_json(file_name, code)


def return_text(file_name, code='utf-8'):
    """
    返回文本文件数据，默认在根目录/static/other/目录下
    :param file_name: 文件名
    :param code: 读取文件编码，默认UTF-8
    :return:
    """
    return _ToolClass.return_text(file_name, code)


def return_css(file_name, code='utf-8'):
    """
    返回CSS数据，默认在根目录/static/css/目录下
    :param file_name: 文件名
    :param code: 读取文件编码，默认UTF-8
    :return:
    """
    return _ToolClass.return_css(file_name, code)


def return_xml(file_name, code='utf-8'):
    """
    返回XML数据，默认在根目录/static/xml/目录下
    :param file_name: 文件名
    :param code: 读取文件编码，默认UTF-8
    :return:
    """
    return _ToolClass.return_xml(file_name, code)


def return_image(file_name):
    """
    返回image数据，默认在根目录/static/image/目录下
    :param file_name: 文件名
    :return:
    """
    return _ToolClass.return_image(file_name)


def return_video(file_name):
    """
    返回video数据，默认在根目录/static/image/目录下
    :param file_name: 文件名
    :return:
    """
    return _ToolClass.return_video(file_name)
