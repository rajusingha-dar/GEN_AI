from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from backend.utils.logger import logger

from dotenv import load_dotenv
load_dotenv()

intent_prompt = PromptTemplate.from_template("""
You are a smart assistant. Classify the user's query into one of the following departments: HR, IT, Analyst, General.
Query: {input}
Department:
""")

llm = ChatOpenAI(temperature=0)
intent_chain: RunnableSequence = intent_prompt | llm  # ✅ new LangChain 0.1.17+ syntax

def classify_intent(user_input: str) -> str:
    try:
        logger.info("Classifying intent for user input")
        result = intent_chain.invoke({"input": user_input})
        logger.info(f"Raw LLM response: {result}")
        return result.content.strip()
    except Exception as e:
        logger.error(f"Intent classification failed: {str(e)}")
        return "General"
