Gemini ChatBot

A simple command-line chatbot built using Google Gemini API in Python. The chatbot interacts with users in real-time and provides AI-generated responses.

🚀 Features

Uses Google Gemini API for responses

Real-time conversation in the terminal

Lightweight and easy to set up

Exit the chat anytime by typing exit

🛠️ Requirements

Python 3.8 or above

google-generativeai Python package

📦 Installation
1. Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2. Install Dependencies
pip install google-generativeai

🔑 Set Up API Key

To use Google Gemini, you need an API key from Google AI Studio:

Go to Google AI Studio

Create or log in to your account

Generate an API key

Replace it in the code:

genai.configure(api_key="YOUR_API_KEY_HERE")

▶️ Run the ChatBot
python ChatBot.py


Usage:

Type your message and hit Enter

Type exit to quit the chatbot

📄 Example Interaction
Welcome to Gemini ChatBot! Type 'exit' to quit.

You: Hello
ChatBot: Hi there! How can I help you today?

🔒 Security Note

Do not upload your API key to GitHub or any public repository.
Instead:

Use environment variables:

set GOOGLE_API_KEY=your_api_key_here  # Windows
export GOOGLE_API_KEY=your_api_key_here  # Linux/Mac


Modify the code:

import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

👤 Contributor

Mubeen Syed
