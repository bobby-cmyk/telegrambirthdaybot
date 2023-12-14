# Birthday Reminder Bot for Telegram
## Overview
This Python script is designed to run a Telegram Bot that sends daily reminders of birthdays. It utilizes a Google Sheets document as a database for storing birthday information and sends notifications through Telegram. The script is hosted on PythonAnywhere and is scheduled to run daily.

## Dependencies
- Python libraries: datetime, pytz, telegram, gspread, os, json, dotenv, pandas.
- A Telegram Bot token and a Google Sheets API setup.
- .env file for securely storing API keys and other sensitive information.
## Setup
- Ensure all Python dependencies are installed.
- Set up a Google Sheet with birthday information and grant access to the Google Sheets API.
- Create a Telegram Bot and obtain the token.
- Store the Google Sheets API credentials, Telegram Bot token, and Telegram chat ID in a .env file.
## Script Features
- Google Sheets Integration: Reads birthday data from a specified Google Sheets document.
- Telegram Bot Integration: Utilizes a Telegram Bot to send birthday reminders.
- Daily Checks: Automatically checks for birthdays every day based on Singapore's timezone.
- Customized Messages: Sends personalized birthday reminders or notifications of upcoming birthdays.
## Functionality
- The script fetches today's date and checks against the birthday list in Google Sheets.
- If there are birthdays today, it sends a birthday reminder to a specified Telegram chat.
- If there are no birthdays today, it checks for the next upcoming birthday and sends a notification.
- The Telegram Bot, running on PythonAnywhere, executes these checks and sends messages daily.
# Usage
This script is ideal for individuals or groups who want to keep track of birthdays and send timely greetings. It's particularly useful for managing birthdays in a community or amongst a group of friends or colleagues.

# Deployment
- The script is hosted on PythonAnywhere, ensuring reliable and consistent daily execution.
- It is set up to run automatically every day without manual intervention.
# Notes
- Adjust the Google Sheets and Telegram Bot configurations as necessary for your specific use case.
- Ensure the script's timezone settings align with your preferred timezone.
- Review and customize the message formats to suit your preference.
