from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="uploadfile.html"
    )
    
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
   with open("destination.png", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   return {"filename": file.filename}