# using gemini
import os
from dotenv import load_dotenv

load_dotenv()
import google.generativeai as genai
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


genai.configure(api_key=GOOGLE_API_KEY)

prompt = """Convert the following sentences to passive voice.
Example 1: The chef cooked the meal → The meal was cooked by the chef.
Example 2: The teacher graded the test → The test was graded by the teacher.
Now convert: The manager approved the project."""


model = genai.GenerativeModel("gemini-2.5-flash")
# Generate content
response = model.generate_content(prompt)

print("Gemini Output:\n", response.text)


# using openai model

# from openai import OpenAI
# openai_api_key = os.getenv("OPENAI_API_KEY")

# client = OpenAI(api_key=openai_api_key)
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user",
#        "content": """Convert the following sentences to passive voice.
#         Example 1: The chef cooked the meal → The meal was cooked by the chef.
#         Example 2: The teacher graded the test → The test was graded by the teacher.
#         Now convert: The manager approved the project."""}
#     ]
# )

# print(response.choices[0].message.content)
