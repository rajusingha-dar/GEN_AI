from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.agents.base_agent import classify_intent
from backend.utils.logger import logger

router = APIRouter()

@router.post("/chat")
async def chat_handler(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        username = request.cookies.get("employee_name", "there")

        if prompt == "__greet__":
            return {"response": f"👋 Hello, {username}! How can I assist you today?"}

        classification = classify_intent(prompt)
        return {"response": f"Based on your query, you're likely seeking {classification} assistance."}

    except Exception as e:
        logger.error(f"Chat handler error: {e}")
        return {"response": "Sorry, something went wrong."}
