import json
from mysql.connector import Error
from flask import Flask, request, Response

default_config = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': False,
}

# 去除空格
def trim(data, key, default = ""):
    value = data.get(key, default)
    if isinstance(value, str):
        return value.strip()
    return value

# 非空校验
def notNull(params):
    """非空校验"""
    if not params:
        raise Error("参数不能为空")
    
# 必须是整数
def isInt(params):
    """必须是整数"""
    if not params or not isinstance(params, int):
        raise Error("参数必须是整数")
    
# 服务
def Service(__name__):
    return Flask(__name__)

# 解析参数
def get_request_data(params="body"):
    if params == "body":
        return request.get_json()
    else:
        return request.args

# 发送数据
def send_data(code=0, msg="数据获取成功。", data=None):
    response_content = {"code": code, "msg": msg}
    if data is not None:
        response_content["data"] = data
    status = 200 if code == 0 else code
    response_json = json.dumps(response_content, ensure_ascii=False)  # 使用json.dumps并设置ensure_ascii=False
    response = Response(response_json, status=status, mimetype='application/json; charset=utf-8')  # 创建Response对象
    return response

# 运行服务
def run(app, config = default_config):
    final_config = {**default_config, **config}
    app.run(**final_config)
