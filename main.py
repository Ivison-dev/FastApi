from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/oi")
def read_oi():
  return {'ivison': 'o cara', 'Quem eu sou': '?'}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

uvicorn.run(app,host="0.0.0.0",port="8080")

#https://github.com/tiangolo/fastapi
#https://tryolabs.com/blog/2019/12/10/top-10-python-libraries-of-2019/