from fastapi import FastAPI, Path, Query

app = FastAPI(title="Path + Query 综合示例")

@app.get("/users/{user_id}/articles", summary="获取用户发布的文章列表")
async def get_user_articles(
    # 路径参数：用户 ID
    user_id: int = Path(..., ge=1, le=10000, description="用户 ID"),
    # 查询参数：分页页码
    page: int = Query(1, ge=1, le=100, description="页码"),
    # 查询参数：每页条数
    size: int = Query(10, ge=1, le=50, description="每页条数"),
    # 查询参数：文章状态（可选）
    status: str = Query("published", pattern=r"^(published|draft)$", description="文章状态：published（已发布）/ draft（草稿）")
):
    return {
        "code": 200,
        "message": "success",
        "data": {
            "user_id": user_id,
            "page": page,
            "size": size,
            "status": status,
            "articles": []
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)