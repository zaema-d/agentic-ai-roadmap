# 🔍 OpenAI Basics – Prompts, Completions, and Temperature

Understanding how Large Language Models (LLMs) like GPT-4 work is key to building Agentic AI.

Let’s break it down.

---

## 📝 What Is a Prompt?

A **prompt** is what you give to the model — a question, instruction, or input text. It's the starting point of the conversation.

Example:

Translate this sentence to French: "I love machine learning."


This is the *prompt*.

## 🎯 What Is a Completion?

A **completion** is what the model generates based on your prompt. It's the response you get back.

Example output from GPT:
J'adore l'apprentissage automatique.

Prompt in → Completion out.

---

## 🎛️ What Is Temperature?

**Temperature** controls the "creativity" of the model's output.

- `temperature = 0.0` → very focused, predictable, deterministic
- `temperature = 1.0` → more random, diverse outputs

Think of it like a spice level 🌶️:
- **0** = plain, safe answer  
- **0.7** = creative and varied  
- **1.0+** = sometimes wild or unexpected

---

## ⚙️ How Does This Work in Code?

You typically send a prompt using OpenAI’s API like this:

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What's the capital of Japan?"}],
    temperature=0.5
)

▶️ Run the OpenAI test script: 
```
python 02_llms_foundation/openai_test.py
```
(after setting your `OPENAI_API_KEY` in a `.env` file)

Resources: https://platform.openai.com/docs/    



