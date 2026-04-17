import openai
import os

def ask(question: str, model: str = None, api_key: str = None) -> str:
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    model = model or os.getenv("LLM_MODEL", "gpt-3.5-turbo")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set!")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": question}],
        max_tokens=512,
    )
    return response.choices[0].message.content.strip()