from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 仅允许指定的前端源（生产环境核心！）
origins = [
    "https://www.your-frontend.com",  # 正式前端域名
    "https://admin.your-frontend.com",  # 管理后台域名
    "http://localhost:3000",  # 临时允许开发环境前端（上线后可移除）
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 仅允许指定源
    allow_credentials=True,  # 允许携带 Cookie（如需）
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 仅允许必要方法
    allow_headers=["Content-Type", "X-Token"],  # 仅允许必要请求头
    expose_headers=["X-Request-ID"],  # 允许前端读取自定义响应头
)

@app.get("/")
def root():
    return {"message": "生产环境跨域配置生效"}