from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from backend.agents.base_agent import base_agent_chain
from backend.utils.logger import logger

class AgentState(BaseModel):
    username: str
    session_id: str
    thread_id: str
    message: str

def build_langgraph_flow():
    try:
        logger.info("Building LangGraph flow...")
        graph = StateGraph(state_schema=AgentState)
        graph.add_node("base", base_agent_chain)
        graph.set_entry_point("base")
        graph.add_edge("base", END)
        return graph.compile()
    except Exception as e:
        logger.error(f"Error building LangGraph flow: {e}")
        raise
