# langchain_chain.py

from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv
import json

load_dotenv()

def get_baby_name_chain(temperature=0.7):
    template = """
You are a baby name assistant. Based on the following inputs, suggest 5 meaningful and creative baby names:

Country of Origin: {country}
Gender: {gender}
Preferred Language of Name: {language}
Starting Alphabet: {letter}
Uniqueness Level: {temperature}
Sibling Name(s): {sibling_name}
Baby Description: {description}

Your goal is to suggest baby names that:
- Match the country and language preference
- Are appropriate for the specified gender
- Begin with the specified alphabet
- Are unique based on the given uniqueness level
- Are distinct from the sibling name(s)
- Align with the baby’s personality and description

Return the result as a JSON list of 5 baby names with fields:
- name
- meaning
- language_of_origin
- vibe_description
- why_it_suits_the_baby

Respond only with valid JSON.
"""

    prompt = PromptTemplate(
        input_variables=["country", "gender", "language", "letter", "temperature", "sibling_name", "description"],
        template=template
    )

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=temperature,
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    return LLMChain(llm=llm, prompt=prompt)


def generate_baby_names(data: dict) -> list[dict]:
    chain = get_baby_name_chain(temperature=data.get("temperature", 0.7))
    
    response = chain.run({
        "country": data.get("country", ""),
        "gender": data.get("gender", ""),
        "language": data.get("language", ""),
        "letter": data.get("letter", ""),
        "temperature": data.get("temperature", 0.7),
        "sibling_name": data.get("sibling_name", ""),
        "description": data.get("description", "")
    })

    # Parse the JSON safely
    try:
        names = json.loads(response)
        return names if isinstance(names, list) else []
    except json.JSONDecodeError:
        return []
