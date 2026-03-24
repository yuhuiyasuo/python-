from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# 自定义中间件1（先注册）
@app.middleware("http")
async def dispatch(request: Request, call_next):
    print("===== Middleware1 ：请求处理前 =====")
    # 调用下一个中间件/路由函数
    response = await call_next(request)
    print("===== Middleware1 ：响应处理后 =====")
    return response

# 自定义中间件2（后注册）
@app.middleware("http")
async def dispatch(request: Request, call_next):
    print("===== Middleware2 ：请求处理前 =====")
    response = await call_next(request)
    print("===== Middleware2 ：响应处理后 =====")
    return response

# 测试路由
@app.get("/test")
async def test():
    print("===== 路由函数执行 =====")
    return {"msg": "success"}


#  http://localhost:8000/test
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)