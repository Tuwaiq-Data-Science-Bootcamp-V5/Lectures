from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("form.html",
                                    {"request": request}
                                    )

@app.post("/", response_class=HTMLResponse)
def analyze_sentiment(request: Request, tweet: str = Form(...)):
    return templates.TemplateResponse(
        "result.html",
        {"request": request, "tweet": tweet},
    )
