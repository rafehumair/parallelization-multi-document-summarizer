from concurrent.futures import ThreadPoolExecutor
from openai import OpenAI  # Replace with Gemini or any provider
import os
from dotenv import load_dotenv
load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Load from .env

def call_llm(prompt: str) -> str:
    """Call OpenAI API to get summary"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def summarize_document(doc: str) -> str:
    """Prepare summarization prompt and get LLM response"""
    prompt = f"Summarize the following document in 5 concise bullet points:\n\n{doc}"
    return call_llm(prompt)

def summarize_documents_parallel(docs: list[str]) -> list[str]:
    """Use parallel execution to summarize all documents"""
    with ThreadPoolExecutor(max_workers=5) as executor:
        summaries = list(executor.map(summarize_document, docs))
    return summaries
