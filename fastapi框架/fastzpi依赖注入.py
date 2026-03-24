from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# app = FastAPI(dependencies=[Depends(verify_token)])  # 全局依赖
# router = APIRouter(dependencies=[Depends(verify_token)])  # 路由器级依赖

# 定义 OAuth2 令牌获取方式（从请求头的 Authorization: Bearer <token> 获取）
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 认证依赖
async def get_current_user(token: str = Depends(oauth2_scheme)):
    # 模拟校验 Token
    fake_users = {"valid_token": {"username": "张三", "id": 1}}
    user = fake_users.get(token)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="无效的令牌",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# 路由注入认证依赖
@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return current_user