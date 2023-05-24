from fastapi import FastAPI
import sqlite3
import uvicorn

banco = sqlite3.connect('teste.db')
cursor = banco.cursor()

cursor.execute("""
  INSERT INTO Pessoas 
  VALUES
  ('ovison', 56, 'ivison@gmail.com')
""")
banco.commit()

app = FastAPI()
cursor.execute("""
      SELECT * FROM Pessoas
""")
t = cursor.fetchall()

@app.get("/")
def read_root():
    
    return {"Hello": t}

@app.get("/oi")
def read_oi():
  return {'ivison': 'o cara', 'Quem eu sou': '?'}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

uvicorn.run(app,host="0.0.0.0",port="8080")

#https://github.com/tiangolo/fastapi
#https://tryolabs.com/blog/2019/12/10/top-10-python-libraries-of-2019/