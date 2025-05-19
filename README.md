# Telegram Bot Demo

This is a simple Telegram bot created using Python and the python-telegram-bot library.

## Features

- `/start` - Displays available commands
- `/about` - Shows information about the bot creator
- `/help` - Provides help information
- `/facts` - Shows interesting facts with interactive buttons

## Setup Instructions

1. Create a new bot and get your token:
   - Open Telegram and search for @BotFather
   - Send /newbot command and follow the instructions
   - Copy the token provided by BotFather

2. Set up environment variables:
   - Create a new file named `.env` by duplicating `.env.example`
   - In the new `.env` file, replace `your_bot_token_here` with your actual bot token
   - Keep both files: `.env.example` is a template, `.env` contains your secret token

3. Set up the environment:
   First, create a virtual environment:
   ```bash
   python -m venv venv
   ```

   Then activate it:
   
   Windows (PowerShell):
   ```powershell
   .\venv\Scripts\activate
   ```
   
   Unix or MacOS:
   ```bash
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the bot:
   ```bash
   python telegram-bot.py
   ```

## Contributing

Feel free to submit issues and enhancement requests.

## License

Licensed under the [MIT License](./LICENSE).