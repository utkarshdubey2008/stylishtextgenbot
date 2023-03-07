
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Replace YOUR_TOKEN_HERE with your bot token
bot = telegram.Bot(token='YOUR_TOKEN_HERE')

# Replace GROUP_OR_CHANNEL_USERNAME with the username of the group or channel you want to force join
group_username = 'GROUP_OR_CHANNEL_USERNAME'

# Replace INVITE_LINK with the invite link to the group or channel
invite_link = 'INVITE_LINK'

# Define the /start command handler
def start(update, context):
    user = update.message.from_user
    chat_id = update.message.chat_id

    # Create an inline keyboard with a "Join Group" button
    keyboard = [[InlineKeyboardButton("Join Group", url=t.me/alphabotupdates)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message to the user with the inline keyboard
    bot.send_message(chat_id=chat_id, text=f"Hi {user.first_name}! Please join the group {group_username} to use this bot.", reply_markup=reply_markup)

# Add the /start command handler to the bot
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start the bot
from telegram.ext import Updater
updater = Updater(token='YOUR_TOKEN_HERE', use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
