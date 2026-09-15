from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}/{age}")
async def hello(name:str,age:int):
   return {"name": name, "age":age} 