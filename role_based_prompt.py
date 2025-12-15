# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load .env
# load_dotenv()
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # Configure Gemini
# genai.configure(api_key=GOOGLE_API_KEY)

# prompt = """You are a professional business analyst.
# Summarize the following article into 3 concise bullet points that highlight key insights:

# Article:
# 'Artificial intelligence is transforming the retail industry by optimizing supply chains, 
# personalizing customer experiences, and enhancing inventory management.'"""

# model = genai.GenerativeModel("gemini-2.5-flash")
# response = model.generate_content(prompt)

# print("Role-Based Summarization Output:\n", response.text)



# using openai
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# 🎯 Role-based prompt
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a professional healthcare analyst who explains insights concisely."},
        {"role": "user", "content": "Summarize this paragraph in one sentence: Artificial intelligence is transforming the healthcare industry by improving diagnostics, personalizing treatments, and streamlining operations."}
    ]
)

print("ChatGPT Role-Based Output:\n", response.choices[0].message.content)
