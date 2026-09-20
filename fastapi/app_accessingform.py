# from fastapi import FastAPI, Form

# app = FastAPI()
# @app.post("/submit/")
# async def submit(nm: str = Form(...), pwd: str = Form(...)):
#    return {"username": nm}


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/hello/{name}", response_class=HTMLResponse)
async def hello(request: Request, name:str):
   return templates.TemplateResponse(
    request=request,
    name="hello.html",
    context={"name": name}
)

   
@app.get("/login/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


class User(BaseModel):
   username:str
   password:str
   
@app.post("/submit/", response_model=User)
async def submit(nm: str = Form(...), pwd: str = Form(...)):
   return User(username=nm, password=pwd)