# Prompt Engineer

This repository is a practical introduction to **Prompt Engineering** using Python and Google Gemini.  
It demonstrates common prompting techniques through simple, runnable examples, making it suitable for beginners as well as developers exploring LLM behavior.

---

## Concepts Covered

The following prompt engineering techniques are implemented in this repository:

- Zero-Shot Prompting  
- Few-Shot Prompting  
- Chain-of-Thought Prompting  
- Role-Based Prompting  

Each technique is implemented in a separate Python script for clarity and ease of understanding.

---

## Repository Structure

```
prompt_engineer/
├── zero_shot_prompting.py
├── few_shot_prompt.py
├── chain_of_thought.py
├── role_based_prompt.py
├── .gitignore
└── README.md
```

---

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/Nawaj2417/prompt_engineer.git
cd prompt_engineer
```

---

### Create and Activate a Virtual Environment

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install python-dotenv google-generativeai
```

---

## Environment Configuration

Create a `.env` file in the project root and add your Gemini API credentials:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

**Important**
- Do not commit the `.env` file to GitHub
- The `.env` file and `venv/` directory are already included in `.gitignore`

---

## Running the Examples

Run any of the following scripts to see different prompt engineering techniques in action:

```bash
python zero_shot_prompting.py
python few_shot_prompt.py
python chain_of_thought.py
python role_based_prompt.py
```

---

## Prompt Engineering Techniques Overview

**Zero-Shot Prompting**  
The model is given a task without any examples.

**Few-Shot Prompting**  
The prompt includes a small number of examples to guide the model’s output.

**Chain-of-Thought Prompting**  
The model is encouraged to reason step-by-step before providing an answer.

**Role-Based Prompting**  
The model is assigned a specific role to influence the style and quality of responses.

---

## Purpose of This Repository

This project aims to:
- Teach core prompt engineering concepts
- Provide practical, executable examples
- Help developers understand LLM prompting behavior
- Serve as a foundation for advanced LLM experimentation

---

## Requirements

- Python 3.8 or higher
- Valid Google Gemini API key

---

## Contributions

Contributions are welcome.  
Feel free to fork the repository, improve prompts, add new techniques, or submit pull requests.

---

## License

This project is open for educational and learning purposes.
