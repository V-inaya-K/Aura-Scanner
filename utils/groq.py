# from groq import Groq
# import os
# from dotenv import load_dotenv
# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# # def ask_groq(query, docs, chat_history):
# #     context = "\n".join([doc.page_content for doc in docs])
# #     print("🔍 Context length:",len(context)) #context length just for sake that data retrived is correct/near to correct
# #     print(context[:500]) # to print the context used

# #     messages = chat_history + [
# #     {
# #         "role": "system",
# #         "content": """
# #         You are an AI assistant analyzing a LinkedIn profile.

# #         Guidelines:
# #         - Use the provided context as the main source
# #         - Try to answer even if information is partial
# #         - Infer reasonable conclusions from available data
# #         - Be confident and helpful
# #         - Avoid saying "Limited information available" unless absolutely necessary
# #         """
# #     },
# #     {
# #         "role": "user",
# #         "content": f"""
# #         Here is the LinkedIn profile data:

# #         {context}

# #         Answer this question:
# #         {query}
# #         """
# #     }
# # ]
# #     response = client.chat.completions.create(
# #         model="llama-3.3-70b-versatile",# using llama-3.3-70b-versatile via groq
# #         messages=messages
# #     )

# #     answer = response.choices[0].message.content

# #     # Memory Feature to groq
# #     chat_history.append({"role": "user", "content": query})
# #     chat_history.append({"role": "assistant", "content": answer})

# #     return answer

# # -------------------------

# def ask_groq(query, docs, chat_history):
#     context = "\n".join([doc.page_content for doc in docs])

#     messages = chat_history + [
#         {
#             "role": "system",
#             "content": """
#             You are an AI assistant analyzing a person's LinkedIn profile and activity.

#             You have access to:
#             - Profile data
#             - Posts
#             - Comments

#             Guidelines:
#             - Use the provided context as the main source
#             - Infer reasonable insights from posts and activity
#             - Answer naturally and helpfully
#             - Avoid saying "Limited information" unless absolutely necessary
#             """
#         },
#         {
#             "role": "user",
#             "content": f"""
#             Context:
#             {context}

#             Question:
#             {query}
#             """
#         }
#     ]

#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=messages
#     )

#     answer = response.choices[0].message.content

#     chat_history.append({"role": "user", "content": query})
#     chat_history.append({"role": "assistant", "content": answer})

#     return answer

# -------------------------

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_groq(query, docs, chat_history):
    context = "\n".join([doc.page_content for doc in docs])

    # 🔥 limit context for better quality
    context = context[:4000]

    messages = chat_history + [
        {
            "role": "system",
            "content": """
            You are an AI assistant analyzing a person's LinkedIn profile and activity.

            You have access to:
            - Profile data
            - Posts
            - Comments
            - Reactions

            Guidelines:
            - Use the context as primary source
            - Infer insights when possible
            - Be confident and helpful
            - Avoid saying "Limited information" unless absolutely necessary

            Rules:
            - Clearly distinguish between POSTS and COMMENTS
            - Posts = content created by the user
            - Comments = replies made by the user
            - Do NOT confuse comments with posts
            """
            
        },
        {
            "role": "user",
            "content": f"""
            Context:
            {context}

            Question:
            {query}
            """
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
    )

    answer = response.choices[0].message.content

    chat_history.append({"role": "user", "content": query})
    chat_history.append({"role": "assistant", "content": answer})

    return answer