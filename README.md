# Discord Chatbot with ChatterBot

This project is a Python-based chatbot that interacts with users on a **Discord server** using **ChatterBot** for AI-driven conversations. It was built to demonstrate real-time chatbot integration in a real-world environment with custom training and performance tracking.

---

## Features

- Real-time responses on Discord
- Custom conversational training via YAML
- Command support: `!info`, `!train`
- Fallback handling for unclear inputs
- Logging of low-confidence responses


Setup Instructions

**Clone the Repository**

```cmd
git clone https://github.com/your-username/discord-chatbot.git
cd discord-chatbot
Install Dependencies

cmd
pip install -r requirements.txt

Configure the Bot

Create a config.py file in the bot/ folder with your bot token:

python
TOKEN = "your-discord-bot-token"
PREFIX = "!"
Run the Bot

cmd
python bot/main.py
