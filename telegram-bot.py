from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext, CallbackQueryHandler
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

async def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hello! I'm your bot. Here are my commands:\n"
                                  "/about - See information about me\n"
                                  "/help - Get help using the bot\n"
                                  "/facts - Get interesting facts\n")

async def about(update: Update, context: CallbackContext):
    """Send information about the bot creator."""
    await update.message.reply_text("I was created by Othmane Moutaouakkil. I'm here to help and share interesting information!")

async def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Here's how to use me:\n"
                                  "- Use /start to see available commands\n"
                                  "- Use /about to learn about me\n"
                                  "- Use /facts to get interesting facts\n"
                                  "Feel free to try these commands!")

async def facts(update: Update, context: CallbackContext):
    """Send interesting facts with inline buttons."""
    keyboard = [
        [InlineKeyboardButton("Next Fact", callback_data='next_fact')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Did you know?\nPython was named after the British comedy group Monty Python!",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: CallbackContext):
    """Handle button callbacks."""
    query = update.callback_query
    await query.answer()
    
    if query.data == 'next_fact':
        facts = [
            "The first version of Python was released in 1991",
            "Python's creator, Guido van Rossum, was also the language's 'Benevolent Dictator for Life' until 2018",
            "Python is one of the official languages at Google"
        ]
        import random
        fact = random.choice(facts)
        keyboard = [[InlineKeyboardButton("Next Fact", callback_data='next_fact')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=f"Did you know?\n{fact}", reply_markup=reply_markup)

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("facts", facts))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
