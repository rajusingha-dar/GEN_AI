from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from backend.openai_sql import generate_sql
from backend.db_config import get_db_connection
from backend.models import PromptRequest
import traceback

app = FastAPI()

# Mount frontend assets
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")


@app.get("/", response_class=HTMLResponse)
def serve_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ask")
def ask_sql(request_data: PromptRequest):
    prompt = request_data.prompt
    print("prompt", prompt)
    try:
        sql_query = generate_sql(prompt)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        result = [dict(zip(columns, row)) for row in rows]
        return {"sql": sql_query, "result": result}
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
