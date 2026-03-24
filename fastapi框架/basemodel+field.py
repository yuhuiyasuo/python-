from typing import Optional
from pydantic import BaseModel, Field
from fastapi import FastAPI

app = FastAPI()

# 子模型：地址信息
class Address(BaseModel):
    province: str = Field(..., min_length=2, max_length=20, example="广东省")
    city: str = Field(..., min_length=2, max_length=20, example="深圳市")
    detail: Optional[str] = Field(None, max_length=100, example="XX小区XX栋")

# 父模型：用户注册信息（嵌套地址模型）
class UserRegister(BaseModel):
    # 关键修正：regex → pattern
    username: str = Field(..., min_length=3, max_length=20, pattern=r"^[a-zA-Z0-9_]+$")
    password: str = Field(..., min_length=6, max_length=32)
    # 关键修正：regex → pattern
    email: str = Field(..., pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    # 嵌套子模型（必填）
    address: Address

# 路由函数：用户注册
@app.post("/users/register/")
async def user_register(user: UserRegister):
    """用户注册（嵌套模型校验）"""
    # 可选优化：v2 推荐用 model_dump() 替代 dict()，功能一致
    user_dict = user.model_dump()
    user_dict.pop("password")
    return {
        "message": "用户注册成功（嵌套校验通过）",
        "user": user_dict
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)