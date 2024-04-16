from typing import Union

from msanic.libs.tool import json_encode, json_parse


def pack_msg(
        cmd_type: (int, str),
        cmd_code: (int, str),
        data: Union[dict, list] = None,
        sta_code: int = 0,
        hint='',
        req=None,
        log_fun=None):
    """
    WS打包消息
    :param cmd_type: 消息命令类型
    :param cmd_code: 消息标识位
    :param data: 消息体数据
    :param sta_code: 响应状态码
    :param hint: 提示信息
    :param req: 客户端消息标记
    :param log_fun: 日志记录方法
    """
    cmd = None
    if isinstance(cmd_code, int) and isinstance(cmd_type, int):
        if 0 <= cmd_code < 1000:
            cmd = cmd_type * 1000 + cmd_code
    if isinstance(cmd_code, str) or isinstance(cmd_type, str):
        cmd = f'{cmd_type}.{cmd_code}'
    if cmd:
        return json_encode({'cmd': cmd, 'data': data, 'code': sta_code, 'req': req, 'hint': hint})
    err_info = f'打包消息出错,消息结构错误: {cmd_type}, {cmd_code},{data},{sta_code},{sta_code},{req}'
    log_fun(err_info) if callable(log_fun) else print(err_info)
    return None


def parse_msg(data, log_fun=None):
    """消息解析"""
    msg = json_parse(data, log_fun=log_fun)
    if (not msg) or (not isinstance(msg, dict)):
        return None, None, None, None
    try:
        cmd = msg.get('cmd')
        if isinstance(cmd, int):
            cmd_type, cmd_code = cmd // 1000, cmd % 1000
        else:
            cmd_type, cmd_code = str(cmd).split('.')
    except Exception as err:
        log_fun(f'{data}消息解析出错：{err}') if log_fun else print(f'{data}消息解析出错：{err}')
        return None, None, None, None
    return cmd_type, cmd_code, json_parse(msg.get('data')), msg.get('req')
