# import os
# from dotenv import load_dotenv
# import google.generativeai as genai


# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=GOOGLE_API_KEY)

# #  Chain-of-Thought prompt
# prompt = """A train travels 60 kilometers in 1 hour. 
# How long will it take to travel 180 kilometers? 
# Let's think step by step before giving the final answer."""

# model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content(prompt)

# print("Gemini Chain-of-Thought Output:\n", response.text)




from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "A train travels 60 kilometers in 1 hour. How long will it take to travel 180 kilometers? Let's think step by step.(no LaTeX)."}
    ]
)

print("ChatGPT Chain-of-Thought Output:\n", response.choices[0].message.content)
