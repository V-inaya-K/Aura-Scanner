from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(query, docs):
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Answer ONLY using the provided LinkedIn data.
    If not found, say "Not available in profile".

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content