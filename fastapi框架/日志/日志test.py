import sys
import time
import uuid
import os
from contextvars import ContextVar
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger
import uvicorn

# 确保日志目录存在
os.makedirs("logs", exist_ok=True)

# 1. 定义请求上下文变量，存储 trace_id
trace_id_ctx: ContextVar[str] = ContextVar("trace_id", default="no-trace-id")


# 2. Loguru patcher：在每条日志记录生成时自动注入 trace_id
def inject_trace_id(record):
    record["extra"]["trace_id"] = trace_id_ctx.get()


# 3. 配置 Loguru
logger.remove()  # 移除默认控制台 handler
logger.configure(patcher=inject_trace_id)  # 全局注入器，确保所有日志都有 trace_id

# 4. 添加各种 Sink（控制台 + 按级别分文件）
# 控制台输出（带颜色，便于开发调试）
logger.add(
    sink=sys.stderr,
    format="<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | {extra[trace_id]} | <level>{level: <8}</level> | {name}:{function}:{line} - <level>{message}</level>",
    level="DEBUG",
    enqueue=False  # 控制台实时输出
)

# 文件按级别分开存储，每个文件 10MB 轮转，保留 30 天
# 为了简洁，这里只展示 DEBUG 和 ERROR，其他级别同理（可自行扩展）
logger.add(
    sink="logs/debug.log",
    level="DEBUG",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {extra[trace_id]} | {level: <8} | {name}:{function}:{line} - {message}",
    filter=lambda record: record["level"].name == "DEBUG"
)
logger.add(
    sink="logs/info.log",
    level="INFO",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {extra[trace_id]} | {level: <8} | {name}:{function}:{line} - {message}",
    filter=lambda record: record["level"].name == "INFO"
)
logger.add(
    sink="logs/warning.log",
    level="WARNING",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {extra[trace_id]} | {level: <8} | {name}:{function}:{line} - {message}",
    filter=lambda record: record["level"].name == "WARNING"
)
logger.add(
    sink="logs/error.log",
    level="ERROR",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {extra[trace_id]} | {level: <8} | {name}:{function}:{line} - {message}",
    filter=lambda record: record["level"].name == "ERROR"
)
logger.add(
    sink="logs/critical.log",
    level="CRITICAL",
    rotation="10 MB",
    retention="30 days",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {extra[trace_id]} | {level: <8} | {name}:{function}:{line} - {message}",
    filter=lambda record: record["level"].name == "CRITICAL"
)

# 5. 测试日志（此时 trace_id_ctx 为默认值 "no-trace-id"，不会报错）
logger.debug("服务启动测试 - DEBUG")
logger.info("服务启动测试 - INFO")
logger.warning("服务启动测试 - WARNING")
logger.error("服务启动测试 - ERROR")
logger.critical("服务启动测试 - CRITICAL")

# ===================== FastAPI 应用 =====================
app = FastAPI(title="Loguru Full-Link Trace Demo")


# 6. 中间件：生成/提取 trace_id 并注入上下文
@app.middleware("http")
async def trace_middleware(request: Request, call_next):
    # 从请求头获取，若无则生成
    trace_id = request.headers.get("X-Trace-Id")
    if not trace_id:
        trace_id = str(uuid.uuid4())
    # 设置到 ContextVar
    token = trace_id_ctx.set(trace_id)

    # 记录请求开始（此时 trace_id 已注入）
    logger.info(f"请求开始 | {request.method} {request.url.path}")
    start_time = time.time()

    try:
        response = await call_next(request)
        # 将 trace_id 写入响应头，便于前端/下游使用
        response.headers["X-Trace-Id"] = trace_id
        cost_ms = (time.time() - start_time) * 1000
        logger.info(
            f"请求结束 | {request.method} {request.url.path} | 耗时 {cost_ms:.2f} ms | 状态码 {response.status_code}")
        return response
    except Exception as exc:
        logger.opt(exception=True).error(f"请求异常 | {request.method} {request.url.path} | {exc}")
        return JSONResponse(
            status_code=500,
            content={"code": 500, "msg": "服务器内部错误", "trace_id": trace_id}
        )
    finally:
        # 重置上下文，避免污染其他请求
        trace_id_ctx.reset(token)


# 7. 测试路由
@app.get("/hello")
async def hello(name: str = "World"):
    logger.info(f"执行 /hello 业务逻辑，name={name}")
    return {"message": f"Hello {name}", "trace_id": trace_id_ctx.get()}


@app.get("/test_error")
async def test_error():
    logger.warning("即将触发除零异常")
    # 故意触发异常
    1 / 0


@app.get("/test_slow")
async def test_slow():
    logger.info("模拟慢请求")
    time.sleep(2)
    return {"message": "slow done", "trace_id": trace_id_ctx.get()}


# 8. 启动服务
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=False  # 生产环境建议关闭
    )