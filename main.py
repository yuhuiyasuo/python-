import time
from fastapi import FastAPI
import uvicorn


app = FastAPI()

# 发送消息接口
@app.post("/messages/")
def send_message():

    time.sleep(5)
    return 'success'


uvicorn.run(app,host='127.0.0.1',port=6000)