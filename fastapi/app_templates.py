# from fastapi.responses import HTMLResponse
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/hello/")
# async def hello():
#    ret='''
#    <html>
#    <body>
#    <h2>Hello World!</h2>
#    </body>
#    </html>
#    '''
#    return HTMLResponse(content=ret)

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request

app = FastAPI()
templates = Jinja2Templates(directory="templates") # 指定模板目录

@app.get("/hello/", response_class=HTMLResponse)
async def hello(request: Request):
   return templates.TemplateResponse("hello.html", {"request": request})