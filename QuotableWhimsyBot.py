from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

Token = "" #insert your Bot Token here

updater = Updater(Token, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""🌟 Welcome to QuotableWhimsyBot! 📜✨
Get inspired with random quotes. Type /quote to receive your daily dose of wisdom!
""")
    
def help(update, context):
    update.message.reply_text("""🤖 QuotableWhimsyBot Help 🤖
- /start -> Starting the bot.
- /help -> This message.
- /quote -> Receive a random quote.
""")
    
def quote(update, context):
    update.message.reply_text(get_data())


def get_data(url="https://api.quotable.io/quotes/random"):
    response = requests.get(url)
    content = response.json()[0]['content']
    author = response.json()[0]['authorSlug']
    return f"""📜 Random Quote:
"{content}"
- {author}
"""

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('quote', quote))

updater.start_polling()
updater.idle()