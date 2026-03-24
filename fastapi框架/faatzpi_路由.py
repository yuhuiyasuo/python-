# routers/users.py
from fastapi import APIRouter, Depends, HTTPException

# 定义依赖函数（token 校验）
def check_token(token: str):
    if token != "valid_token":
        raise HTTPException(status_code=401, detail="无效的 Token")
    return token

# 实例化 Router 时添加公共依赖
router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(check_token)],  # 该模块所有路由都需校验 token
)

# 所有用户路由自动触发 token 校验，无需手动加 Depends
@router.get("/")
def get_users():
    return [{"id": 1, "name": "张三"}]