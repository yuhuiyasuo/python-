import uvicorn
from fastapi import FastAPI, Depends, Path

app = FastAPI()


@app.get("/")
def root():
    return "root return"

@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(
        ...,  # ... 表示必填（路径参数默认必填，可省略）
        ge=1,  # 最小值1
        le=1000,  # 最大值1000
        title="商品ID",
        description="商品的唯一标识，范围1~1000"
    )
):
    return {"item_id": item_id}



if __name__ == "__main__":



    uvicorn.run("基本写法:app", host="127.0.0.1", port=8000, reload=True)