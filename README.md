Prompt Engineer 🧠✨
A hands-on guide to Prompt Engineering with Python & Google Gemini

This repository is a practical, beginner-friendly introduction to prompt engineering, featuring minimal, runnable examples that demonstrate core prompting techniques using the Google Gemini API. Perfect for developers, educators, and AI enthusiasts eager to level up their LLM interaction skills.

📌 What You’ll Learn
Each technique is implemented in a standalone, easy-to-understand Python script:

Technique
File
Description
Zero-Shot Prompting
zero_shot_prompting.py
Direct task instructions—no examples.
Few-Shot Prompting
few_shot_prompt.py

Provide examples to steer model behavior.
Chain-of-Thought
chain_of_thought.py
Encourage step-by-step reasoning.
Role-Based Prompting
role_based_prompt.py
Assign personas (e.g., expert, teacher) for context-aware responses.
✅ All examples are self-contained, require only a Gemini API key, and run in <10 seconds.

📂 Project Structure
1234567
prompt_engineer/
├── zero_shot_prompting.py
├── few_shot_prompt.py
├── chain_of_thought.py
├── role_based_prompt.py
├── .gitignore
└── README.md
No external data or complex dependencies — just pure prompt engineering fundamentals.

⚙️ Quick Setup
1. Clone the repo
bash
12
git clone https://github.com/Nawaj2417/prompt_engineer.git
cd prompt_engineer
2. Set up virtual environment
bash
1234567
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
1
pip install python-dotenv google-generativeai
4. Add your Gemini API key
Create a .env file in the project root:

env
1
GEMINI_API_KEY=your_gemini_api_key_here
🔒 Security Note: .env is in .gitignore — never commit secrets!

5. Run any example
bash
12345
python zero_shot_prompting.py
# or
python few_shot_prompt.py
python chain_of_thought.py
python role_based_prompt.py
🧠 Prompting Techniques at a Glance
Technique
When to Use
Zero-Shot
Simple, well-defined tasks (e.g., classification, summarization).
Few-Shot
Ambiguous tasks needing format/style guidance.
Chain-of-Thought
Math, logic, or multi-step reasoning problems.
Role-Based
When tone, expertise, or perspective matters (e.g., tutoring, customer support).
💡 Pro Tip: Combine techniques! Try Few-Shot + Chain-of-Thought for complex tasks.

🎯 Goals of This Project
✅ Teach prompt engineering through executable examples, not just theory
✅ Lower the barrier to entry for LLM development
✅ Provide a reusable foundation for experimentation and prototyping
✅ Promote secure, responsible API usage (.env, .gitignore, no hard-coded keys)
🛡️ Security Best Practices
API keys stored in .env (never in source code)
.env, venv/, and IDE files excluded via .gitignore
Minimal dependencies — reduces attack surface
🤝 Want to Contribute?
We welcome contributions! Here’s how you can help:

✨ Add new prompting strategies (e.g., Self-Consistency, ReAct, Tree-of-Thoughts)
📝 Improve prompts (clarity, robustness, edge cases)
🧪 Add unit/integration tests
🌐 Localize examples or add multilingual prompts
📚 Enhance documentation (tutorials, diagrams, use cases)
👉 Fork → Branch → PR! Open issues for discussion.

📎 Requirements
Python ≥ 3.8
Google AI Studio Account & Gemini API Key
Internet connection (for API calls)
