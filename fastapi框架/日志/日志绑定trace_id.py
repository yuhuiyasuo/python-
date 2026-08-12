import uuid
from contextvars import ContextVar
import sys
import uvicorn
from fastapi import FastAPI, Request
from loguru import logger

# 1. 请求上下文变量，存储trace_id
trace_id_ctx: ContextVar[str] = ContextVar("trace_id", default="no-trace-id")

# 2. 日志简单配置
logger.remove()

# ========== 新增：控制台输出配置 ==========
logger.add(
    sink=sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {extra[trace_id]} | {message}"
)

# 文件输出配置（原有不变）
logger.add(
    sink="app.log",
    rotation="10MB",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {extra[trace_id]} | {message}"
)

# 简易工具：打印日志时自动带上trace_id
def get_logger():
    return logger.bind(trace_id=trace_id_ctx.get())

app = FastAPI()

# 3. 中间件：每个请求生成trace_id
@app.middleware("http")
async def trace_middleware(request: Request, call_next):
    # 优先取请求头，没有就新建
    trace_id = request.headers.get("X-Request-Id", str(uuid.uuid4()))
    token = trace_id_ctx.set(trace_id)

    log = get_logger()
    log.info(f"收到请求 {request.method} {request.url.path}")
    try:
        resp = await call_next(request)
        resp.headers["X-Request-Id"] = trace_id
        log.info(f"请求结束 status={resp.status_code}")
        return resp
    except Exception as e:
        log.opt(exception=True).error("请求异常")
        raise
    finally:
        trace_id_ctx.reset(token)


# 测试接口
@app.get("/demo")
async def demo_api():
    log = get_logger()
    log.info("进入demo接口")
    service_func()
    return {"msg": "success"}


# 模拟下层业务函数
def service_func():
    log = get_logger()
    log.info("执行业务逻辑")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)