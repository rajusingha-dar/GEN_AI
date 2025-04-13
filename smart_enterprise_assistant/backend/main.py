from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.routes import auth, chat
from backend.utils.logger import logger

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend/src/static"), name="static")
templates = Jinja2Templates(directory="frontend/src/templates")

app.include_router(auth.router, prefix="/api/auth")
app.include_router(chat.router, prefix="/api")

# Allow cross-origin requests for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    try:
        logger.info("Rendering login page")
        return templates.TemplateResponse("login.html", {"request": request})
    except Exception as e:
        logger.error(f"Error rendering login page: {e}")
        return HTMLResponse(content="Internal Server Error", status_code=500)

@app.get("/signup", response_class=HTMLResponse)
def read_signup(request: Request):
    try:
        logger.info("Rendering signup page")
        return templates.TemplateResponse("signup.html", {"request": request})
    except Exception as e:
        logger.error(f"Error rendering signup page: {e}")
        return HTMLResponse(content="Internal Server Error", status_code=500)

@app.get("/chat", response_class=HTMLResponse)
def chatbot_page(request: Request):
    try:
        logger.info("Rendering chatbot page")

        # Retrieve username from cookies (must match how you set it after login)
        username = request.cookies.get("employee_name")
        logger.info(f"Chatbot page username from cookie: {username}")

        return templates.TemplateResponse("chatbot.html", {
            "request": request,
            "username": username if username else ""
        })
    except Exception as e:
        logger.error(f"Error rendering chatbot page: {e}")
        return HTMLResponse(content="Internal Server Error", status_code=500)
