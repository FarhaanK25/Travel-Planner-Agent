import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_llm(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": """
You are an advanced AI Travel Planning Agent.

Your job is to:
Plan complete travel itineraries
Suggest hotels
Estimate travel budgets
Provide day-wise activity planning
Provide cost breakdowns
S
uggest restaurants and transport options

Always produce structured and detailed travel plans.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 1200
    }

    try:
        response = requests.post(URL, headers=headers, json=data)

        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"LLM Error: {str(e)}"