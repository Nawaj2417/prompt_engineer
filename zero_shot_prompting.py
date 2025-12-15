import os
from dotenv import load_dotenv
import google.generativeai as genai
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

gemini_model = genai.GenerativeModel("gemini-2.5-flash")
gemini_response = gemini_model.generate_content("Summarize the article in one sentence about quantum computing in simple terms.")

print("Gemini Output:\n", gemini_response.text)





# # using chatgpt

# from openai import OpenAI
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=openai_api_key)
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user",
#         "content": "Summarize this paragraph in one sentence: Artificial intelligence is transforming the healthcare industry by improving diagnostics, personalizing treatments, and streamlining operations."}
#     ]
# )

# print(response.choices[0].message.content)
