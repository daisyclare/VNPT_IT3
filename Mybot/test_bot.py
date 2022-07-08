import Constants as keys
import Response as R
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Filters
import json
import sys
sys.path.append('Method/News')
import News

print("Bot Starting....")

def start_command(update: Update, context: CallbackContext) -> None:
  update.message.reply_text(f'Chào {update.effective_user.first_name}')

def help_command(update: Update, context: CallbackContext):
  update.message.reply_text("Bạn muốn tôi giúp gì? \nXEM BÓI -> /here ")

def news_command(update: Update, context: CallbackContext):
  try:
    limit_news = int(context.args[0])
    here = News.GetNews(limit_news)
    for x in range(0, len(here)): 
      message = json.loads(here[x])
      update.message.reply_text(message['title'] + "\n" 
        + message['link'] + "\n" + message['description'])
  except (IndexError, ValueError):
    update.message.reply_text('Hôm nay là ngày may mắn của bạn \nHãy tận hưởng ngày nó ngay đi nhé <3')

def handle_message(update: Update, context: CallbackContext):
  text = str(update.message.text).lower()
  response = R.sample_response(text)
  update.message.reply_text(response)

def error(update: Update, context: CallbackContext):
  print(f"Update {update} cause error {context.error}")

import telegram
def send_test_message():
    try:
        telegram_notify = telegram.Bot("5450451813:AAE9j0l_2LktXEqa336bJtzzOx87XWi0PLI")
        message = "Hello everyone, Welcome to mybot" 
    
        telegram_notify.send_message(chat_id="-732632952", text=message,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)

def main():
  updater = Updater(keys.API_KEY, use_context=True)
  dp = updater.dispatcher
  dp.add_handler(CommandHandler("hi", start_command))
  dp.add_handler(CommandHandler("help", help_command))
  dp.add_handler(CommandHandler("here", news_command))
  dp.add_handler(MessageHandler(Filters.text, handle_message))
  dp.add_error_handler(error)

  updater.start_polling()
  updater.idle()

send_test_message()
main()
