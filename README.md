# 🛡️ AI Security Assistant

A sleek command-line tool that blends **cybersecurity fundamentals** with **AI-powered explanations** via OpenAI's GPT. Designed for learners, professionals, and cyber-curious baddies who want to study smart and build smarter.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT3.5-brightgreen?logo=openai)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## ⚙️ Features

✨ **Password Strength Checker**  
Evaluate the strength of a password and get simple, readable feedback.

🧠 **GPT-Powered Concept Explainer**  
Ask the assistant anything about cybersecurity: MFA, Zero Trust, CIA Triad, you name it.

🔐 **Base64 Encoder/Decoder**  
Encode or decode strings using Base64 in seconds.

💻 **Easy-to-Use CLI Interface**  
Simple, menu-driven interaction — beginner friendly but dev-worthy.

---

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/PreciousDeanna/ai-security-assistant.git
cd ai-security-assistant

# Create & activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install openai==0.28 python-dotenv termcolor

## 🔑 Setup
Create a .env file in the root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=sk-your-key-here

## 🧪 How to Use
python3 main.py

# You’ll be prompted with a clean CLI interface:
🛡️  AI Security Assistant
1. Check password strength
2. Explain a security concept with GPT
3. Base64 Encode/Decode a string
4. Exit

## 📸 Screenshot
Here’s what the assistant looks like in action:

### Encoder
![AI Security Assistant in Terminal](screenshot4.png)

### GPT Explanation Example
![AI Security Assistant in Terminal](screenshot3.png)
