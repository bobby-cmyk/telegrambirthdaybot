from datetime import *
from pytz import *
from telegram import *
from telegram.ext import *
import gspread
import os
import json
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Setting up Authentication for Google Sheet API
google_api_json = os.getenv('google_api')
google_api = json.loads(google_api_json)
gc = gspread.service_account_from_dict(google_api)

# Setting up authentication for Telegram Bot
telegram_token = os.getenv('api_key')
bot = Bot(token=telegram_token)

# Chat ID for TeleBot to send messages to
chat_id = os.getenv('chat_id')

# Open the Google Sheet
sheet = gc.open("Birthday List").worksheet("Birthday List")
# Load sheet as a datafram
df = pd.DataFrame(sheet.get_all_records())

# Today's timing (Singapore's Timezone)
today = datetime.now(timezone('Asia/Kuala_Lumpur'))
today_string = today.strftime("%d/%m")

# Filter out rows of today's birthdays
bday_df = df[df["Birthday"] == today_string].reset_index(drop=True)

# Function to generate message if there's birthdays today 
def bday_message(chat_id, df_bday):
  # Loop through birthdays/birthday adn retrive name of birthday person
  for i in range(0,len(bday_df)):
    name = df_bday["Name"][i]
    message = f"It's {name}'s birthday today! Send a message! 🎂🎉"
    bot.send_message(chat_id=chat_id, text=message)

# Function to generate message if there's no birthdays today
def no_bday_message(chat_id, df):
  # Filter out birthdays that are after today
  future_df = df[df["Birthday"]>today_string].reset_index(drop=True)

  # If there are no more birthdays after today
  if future_df.empty:
    name_next_bday = df["Name"][0]
    date_next_bday = df["Birthday"][0]

  else:
    name_next_bday = future_df["Name"][0]
    name_next_bday = future_df["Birthday"][0]
    
  message = f"No birthdays today. {name_next_bday}'s is coming up next on {date_next_bday}!"
  bot.send_message(chat_id=chat_id, text=message)

# Start Telegram Bot
updater = Updater(telegram_token, use_context=True)
updater.start_polling()

#If no birthdays today, send no birthday message
if bday_df.empty:
  no_bday_message(chat_id, df)
#else send birthday message
else:
  bday_message(chat_id, bday_df)

# Stop Telegram Bot
updater.stop()