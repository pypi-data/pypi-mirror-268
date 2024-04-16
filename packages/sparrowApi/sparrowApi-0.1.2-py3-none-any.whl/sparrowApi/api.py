import inspect
import pprint
import socket
import datetime
import threading
from colorama import Fore, init
from sparrowApi.constant import ContentType, Main


class SparrowApi(threading.Thread):
    def __init__(self, name=__name__):
        self._is_cors_ = False
        self._is_save_log_ = True
        init(autoreset=True)
        threading.Thread.__init__(self)
        self._name_ = name
        self._default_listen_ = 20
        self._content_type_ = ContentType.TEXT
        self._host_ = ""
        self._port_ = ""
        self._debug_ = False
        self._routes_ = {}
        self._show_routes_ = []
        self._log_file_ = ""

    def _log_(self, save_data):
        """
        日志记录
        :param save_data: 需要记录的日志内容
        :return:
        """
        if self._is_save_log_:
            with open(self._log_file_, 'a', encoding='utf-8') as f:
                f.write(f"{save_data}\n")

    def _register_(self, path: str, func, method: str, content_type: dict) -> None:
        """
        路由注册
        :param path: 路由
        :param func: 与路由绑定的方法
        :param method: 此路由的请求方法
        :param content_type: content_type的类型
        :return:
        """
        content_type_str = ""
        for k, v in content_type.items():
            content_type_str += f"{k}: {v}\r\n"
        if self._is_save_log_:
            content_type_str += "Access-Control-Allow-Origin: *\r\n"
        if f"{path}" in self._routes_.keys():
            if method in self._routes_[path].keys():
                raise Exception(
                    f"{str(datetime.datetime.now()).split('.')[0]} path:{path} -> function:{func.__name__}() not _register_ because {self._routes_[path]['methods'][method].__name__}() use {method} method already in {self._name_}")
            else:
                self._show_routes_.append({path: method})
                self._routes_[path][method] = {"func": func, "content_type": content_type_str}
                self._routes_[path][method]['func'] = func
                self._routes_[path][method]['content_type'] = content_type_str
        else:
            self._show_routes_.append({path: method})
            self._routes_[path] = {method: {"func": func, "content_type": content_type_str}}

    def route(self, path: str = '/', methods: list = None, content_type: dict = None):
        """
        基础路由设置
        :param path: 默认路由地址为/
        :param methods: 默认请求方法为GET，POST，PUT，DELETE，PATCH，HEAD，OPTIONS
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if methods is None:
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS']
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            for method in methods:
                self._register_(path, func, method, content_type)
            return func

        return decorator

    def get(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为GET
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "GET", content_type)
            return func

        return decorator

    def post(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为POST
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "POST", content_type)
            return func

        return decorator

    def head(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为HEAD
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "HEAD", content_type)
            return func

        return decorator

    def options(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为OPTIONS
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "OPTIONS", content_type)
            return func

        return decorator

    def put(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为PUT
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "PUT", content_type)
            return func

        return decorator

    def delete(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为DELETE
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "DELETE", content_type)
            return func

        return decorator

    def patch(self, path: str = '/', content_type: dict = None):
        """
        路由设置，请求方法为PATCH
        :param path: 默认路由地址为/
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :return:
        """
        if content_type is None:
            content_type = self._content_type_

        def decorator(func):
            self._register_(path, func, "PATCH", content_type)
            return func

        return decorator

    def _return_(self, request, client_socket, path_, address, handler, content_type, headers, method):
        """
        解析数据以及返回数据
        :param request: socket的获取到的数据
        :param client_socket: socket服务
        :param path_: 路由地址
        :param address: 发送求情的地址
        :param handler: 路由绑定的方法
        :param content_type: 返回数据的类型
        :param headers: 请求头
        :param method: 请求方法
        :return:
        """
        data = {}
        new_body = ""
        if len(path_.split("?")) == 2:
            parameter = path_.split("?")[1]
            new_body = self._decode_url_parameter_(parameter)
        request_post_data = request.split("\r\n\r\n")[-1]
        for one_data in request_post_data.split("&"):
            if len(request_post_data.split("&")) > 0 and request_post_data.split("&")[0] != "":
                data[one_data.split("=")[0]] = one_data.split("=")[1]
        parameter_num = len(inspect.signature(handler).parameters)
        parameter_list = list(inspect.signature(handler).parameters)
        response = None
        if parameter_num == 0:
            response = handler()
        elif parameter_num == 1:
            if "data" in parameter_list:
                response = handler(data=data)
            elif "headers" in parameter_list:
                response = handler(headers=headers)
            elif "body" in parameter_list:
                response = handler(args=new_body)
        elif parameter_num == 2:
            if sorted(parameter_list) == sorted(["data", "args"]):
                response = handler(data=data, args=new_body)
            elif sorted(parameter_list) == sorted(["data", "headers"]):
                response = handler(data=data, headers=headers)
            elif sorted(parameter_list) == sorted(["args", "headers"]):
                response = handler(headers=headers, args=new_body)
        elif parameter_num == 3:
            response = handler(data=data, headers=headers, args=new_body)
        response = f"HTTP/1.1 200 OK\r\n{content_type}\r\n{response}"
        client_socket.sendall(response.encode('utf-8'))
        message = f"{str(datetime.datetime.now()).split('.')[0]} from {address[0]}:{address[1]} to http://{self._host_}:{self._port_}{path_} {method} successful"
        print(message)
        self._log_(message)

    def run(self, host: str = "127.0.0.1", port: int = 7012, try_model: bool = True, show_error: bool = True,
            log_file: str = "%s.log", default_listen: int = Main.MAX_LISTEN, is_save_log: bool = True,
            content_type: dict = ContentType.TEXT, show_register: bool = False, is_cors: bool = False):
        """
        sparrowApi启动程序
        :param is_cors: 是否允许跨域
        :param is_save_log: 是否进行日志记录
        :param show_register: 运行时是否输出已注册的路由路径
        :param content_type: 发送的数据类型，默认为text，基础类型在ContentType中，可以自定义，同时也为所有的请求头，传入类型为dict
        :param default_listen: 最大连接数，默认20
        :param host: 对外输出网址，默认网址为127.0.0.1
        :param port: 对外输出端口，默认端口为7012
        :param try_model: 是否开启try模式，开启后默认进行日志记录，True为开启，False为关闭
        :param show_error: 是否显示错误信息，True为开启，False为关闭，此模式的开启需要开启try模式
        :param log_file: 日志存放文件，默认为名称为当前日期，此模式的开启需要开启try模式
        :return: 
        """
        self._is_cors_ = is_cors
        self._is_save_log_ = is_save_log
        self._content_type_ = content_type
        self._default_listen_ = default_listen
        self._host_ = host
        self._port_ = port
        if show_register:
            pprint.pprint(self._show_routes_)
        if try_model:
            print(f"* try_model is True")
        else:
            print(Fore.RED + "try_model is False please change True")
        print(f"* {str(datetime.datetime.now()).split('.')[0]} Server SparrowApi started on {self._name_}")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self._host_, self._port_))
            server_socket.listen(Main.MAX_LISTEN)
            print(
                Fore.RED + f"* {str(datetime.datetime.now()).split('.')[0]} Server is running on http://{self._host_}:{self._port_}")
            while True:
                client_socket, addr = server_socket.accept()
                if try_model:
                    try:
                        self._handle_request_(client_socket, addr)
                    except Exception as e:
                        response = 'HTTP/1.1 404 Not Found\r\nContent-Type: */*\r\n\r\nParameter Not Bad'
                        client_socket.sendall(response.encode('utf-8'))
                        client_socket.close()
                        if log_file == "%s.log":
                            self._log_file_ = "%s.log" % (str(datetime.datetime.now()).split('.')[0].split(' ')[0])
                        else:
                            self._log_file_ = log_file
                        if show_error:
                            print(f"{str(datetime.datetime.now()).split('.')[0]} {e}")
                        self._log_(f"{str(datetime.datetime.now()).split('.')[0]} {e}")
                else:
                    self._handle_request_(client_socket, addr)

    def _decode_url_parameter_(self, url_parameter: str):
        """
        解析Get请求发送的参数
        :param url_parameter: 发送数据的url
        :return:
        """

        class BaseClass(object):
            def get(self, key_name):
                return getattr(self, key_name)

            def set(self, data: dict):
                for key_name, value_name in data.items():
                    setattr(self, key_name, value_name)

        parameters = url_parameter.split("&")
        result = BaseClass()
        for parameter in parameters:
            key, value = parameter.split("=")[0], parameter.split("=")[1]
            result.set({key: value})
        return result.__dict__

    def _decode_header_(self, request):
        """
        解析请求头
        :param request: socket获取的数据
        :return:
        """
        headers_dict = {}
        headers = request.split("\r\n\r\n")[0].split("\r\n")[1:]
        for header in headers:
            key, value = header.split(": ")
            headers_dict[key] = value
        return headers_dict

    def _handle_request_(self, client_socket, address):
        """
        socket运行主方法
        :param client_socket: socket服务
        :param address: 请求发动的地址
        :return:
        """
        request_data = client_socket.recv(4096)
        if not request_data:
            return
        request = request_data.decode('utf-8')
        headers = self._decode_header_(request)
        request_line, _, _ = request.partition('\r\n')
        http_method, path_, _ = request_line.split(' ', 2)
        path = path_.split("?")[0]
        if path == "/favicon.ico":
            pass
        else:
            if path in self._routes_.keys():
                if http_method in self._routes_[path].keys():
                    handler = self._routes_.get(path).get(http_method).get("func")
                    content_type = self._routes_.get(path).get(http_method).get("content_type")
                    self._return_(request, client_socket, path_, address, handler, content_type, headers, http_method)
                else:
                    response = 'HTTP/1.1 404 Not Found\r\nContent-Type: */*\r\n\r\nMethod Is Error'
                    client_socket.sendall(response.encode('utf-8'))
                    message = f"{str(datetime.datetime.now()).split('.')[0]} from {address[0]}:{address[1]} to http://{self._host_}:{self._port_}{path_} {http_method} unsuccessful"
                    print(message)
                    self._log_(message)
            else:
                response = 'HTTP/1.1 404 Not Found\r\nContent-Type: */*\r\n\r\nPath Not Found'
                client_socket.sendall(response.encode('utf-8'))
                message = f"{str(datetime.datetime.now()).split('.')[0]} from {address[0]}:{address[1]} to http://{self._host_}:{self._port_}{path_} {http_method} unsuccessful"
                print(message)
                self._log_(message)
            client_socket.close()
