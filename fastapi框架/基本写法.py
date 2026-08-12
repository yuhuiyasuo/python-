import uvicorn
from fastapi import FastAPI, Depends, Path

app = FastAPI()



@app.get("/{item_id}")
def read_item(
    item_id: int
):
    print(item_id)
    print("===========")
    return {"item_id": item_id}
    return {"item_id": item_id}



if __name__ == "__main__":



    uvicorn.run("基本写法:app", host="127.0.0.1", port=8000, reload=True)