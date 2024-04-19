from contextvars import ContextVar

# 申明应用ID变量
app_id = ContextVar('Id of app', default="")

# 申明请求ID变量
request_id = ContextVar('Id of request', default="")
