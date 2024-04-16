class WsConnector:
    """Websocket连接管理器"""

    __COMM_MAP = {}

    @classmethod
    def all_ws(cls):
        return cls.__COMM_MAP.values()

    @classmethod
    def get_ws(cls, key: (str, int, bytes)):
        return cls.__COMM_MAP.get(key)

    @classmethod
    async def set_ws(cls, key: (str, int, bytes), ws):
        """更新连接，如果存在旧连接会关闭旧连接"""
        old_ws = cls.get_ws(key)
        cls.__COMM_MAP[key] = ws
        old_ws and await old_ws.close()

    @classmethod
    async def close_ws(cls, key: (str, int, bytes), msg: (str, bytes) = None):
        ws = cls.get_ws(key)
        if ws:
            cls.__COMM_MAP.pop(key)
            msg and await ws.send(msg)
            await ws.close()


class HeaderSet:

    RESP_TYPE = {
        'JSON': 'application/json',
        'MSGPACK': 'text/msgpack',
        'TEXT': 'text/plain',
        'HTML': 'text/html',
    }

    @classmethod
    def out(cls, conf):
        tp = cls.RESP_TYPE.get(conf.RESP_TYPE)
        if not tp:
            raise Exception('无效的响应类型配置')
        if conf.RESP_TYPE != 'MSGPACK':
            tp += f';charset={conf.CHARSET}'
        headers = {
            'Content-Type': tp,
            'Access-Control-Allow-Methods': ','.join(conf.ALLOW_METHOD),
            'Access-Control-Max-Age': conf.ORIGIN_MAX_AGE,
            'Access-Control-Allow-Headers': '*' if '*' in conf.ALLOW_HEADER else ','.join(conf.ALLOW_HEADER),
            'Access-Control-Allow-Origin': '*' if '*' in conf.ALLOW_ORIGIN else ','.join(conf.ALLOW_ORIGIN),
            'Access-Control-Allow-Credentials': conf.ALLOW_CREDENTIALS
        }
        return headers
