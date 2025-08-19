from fastapi import APIRouter
from pydantic import BaseModel
from ..rag import rag_pipeline 

router = APIRouter()

class ChatQuery(BaseModel):
    question: str

def generate_simple_response(prompt: str) -> str:
    try:
        context_start = prompt.index("Context:") + len("Context:")
        context_end = prompt.index("Question:")
        context = prompt[context_start:context_end].strip()
        
        return f"Based on the information I found: {context}"
    except ValueError:
        return "I couldn't find specific information for that question, but I can help with general fitness topics."


@router.post('/chat', tags=['chat'])
async def handle_chat(query: ChatQuery):
    if rag_pipeline is None:
        return None
    
    try:
        formatted_prompt_object = rag_pipeline.invoke(query.question)
        final_answer = generate_simple_response(formatted_prompt_object.to_string())
        
        return {"user_question": query.question, "answer": final_answer}
    except Exception as e:
        return None