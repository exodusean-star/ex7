from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(root_path="/api")  # ← 이거 추가

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,        # ← 이렇게 변경
        name="index.html",
        context={
            "title": "ST1 FastAPI",
            "message": "EKS + ALB로 서빙 중입니다!"
        }
    )

@app.get("/health")
async def health():
    return {"status": "ok"}