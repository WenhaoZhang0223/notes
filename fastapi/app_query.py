
# app = FastAPI()
# @app.get("/hello")
# async def hello(name:str,age:int):
#    return {"name": name, "age":age}


from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def hello(name:str,age:int):
   return {"name": name, "age":age}