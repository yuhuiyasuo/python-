
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()


call_count = 0

def get_config():
    global call_count
    call_count += 1
    print(f"get_config 被调用第 {call_count} 次")
    return {"secret": "xxx"}

def dep_a(config: dict = Depends(get_config)):
    return f"A: {config}"

def dep_b(config: dict = Depends(get_config)):
    return f"B: {config}"

@app.get("/test")
async def test(
    a = Depends(dep_a),
    b = Depends(dep_b)
):
    # get_config 只会被调用 1 次！
    # 因为 use_cache=True（默认）
    return {"a": a, "b": b}

#  http://localhost:8000/test
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)