# 📚 Oxford 3000 Telegram Bot

A Python-based Telegram bot that randomly sends 10 new English words from the "Oxford 3000" list every 24 hours. The bot is designed to keep track of previously sent words to ensure they are not repeated in the future.

## 🚀 Features
- **Automated Delivery:** Sends 10 words automatically every 24 hours.
- **Duplicate Prevention:** Tracks sent words in a `used_words.json` file to guarantee no word is sent twice.
- **Neat Formatting:** Displays the words in a clean, numbered list along with their part of speech (noun, verb, adjective, etc.).
- **Background Execution:** Can be hosted on a server to run continuously without manual intervention.

## 📋 Prerequisites
Ensure you have the following installed and set up before running the bot:
- [Python 3.6+](https://www.python.org/downloads/)
- The `requests` library (installation command below).
- **Bot Token:** You can get this from [BotFather](https://t.me/botfather) on Telegram.
- **Chat ID:** The ID of the channel, group, or personal chat where the bot will send the words.

## 🛠️ Installation & Setup

 - **Install required libraries:**
   Open your terminal and run the following command:
   ```bash
   pip install requests 

## 1.Prepare the words file (oxford_words.json):
Make sure you have a file named oxford_words.json in the same directory as the script. It must be in JSON format and structured like this example:
```bash
[
  {"word": "ability", "pos": "noun"},
  {"word": "able", "pos": "adjective"}
]
```

## 2.Set Environment Variables:
You need to set the following environment variables to securely store your credentials:

TELEGRAM_BOT_TOKEN: Your bot's token.

TELEGRAM_CHAT_ID: Your target chat ID.

On Linux/macOS:
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"
```
On Windows (Command Prompt):
```bash
set TELEGRAM_BOT_TOKEN="your_bot_token_here"
set TELEGRAM_CHAT_ID="your_chat_id_here"
```

## ▶️ How to Run
Once the variables and the words file are set up, run the script using:
```bash
python bot.py
```
The bot will start, immediately send the first 10 words, print Sent 10 words. Next run in 24 hours. in the console, and then sleep for exactly 24 hours before sending the next batch.

## 📂 File Structure
bot.py: The main script containing the bot's code.

oxford_words.json: The complete list of words (you must provide this).

used_words.json: An automatically generated file that logs the words that have already been sent.
