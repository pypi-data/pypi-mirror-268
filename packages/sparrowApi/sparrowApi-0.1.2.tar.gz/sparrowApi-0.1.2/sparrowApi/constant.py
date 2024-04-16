class ContentType:
    """
    ContentType默认数据
    """
    TEXT = {"Content-Type": "text/plain"}
    HTML = {"Content-Type": "text/html"}
    CSS = {"Content-Type": "text/css"}
    JAVASCRIPT = {"Content-Type": "text/javascript"}
    JSON = {"Content-Type": "application/json"}
    XML = {"Content-Type": "application/xml"}
    OCTET_STREAM = {"Content-Type": "application/octet-stream"}
    JPEG = {"Content-Type": "image/jpeg"}
    GIF = {"Content-Type": "image/gif"}
    PNG = {"Content-Type": "image/png"}
    MP3 = {"Content-Type": "audio/mpeg"}
    MP4 = {"Content-Type": "video/mp4"}
    FROM_DATA = {"Content-Type": "multipart/form-data"}
    URL_CODE = {"Content-Type": "application/x-www-form-urlencoded"}


class Main:
    """
    主要的固定参数
    """
    MAX_LISTEN = 20
