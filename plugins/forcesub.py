from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace YOUR_API_ID and YOUR_API_HASH with your API ID and API Hash
app = Client("my_bot", api_id=YOUR_API_ID, api_hash=YOUR_API_HASH)

# Replace GROUP_OR_CHANNEL_USERNAME with the username of the group or channel you want to force join
group_username = 'GROUP_OR_CHANNEL_USERNAME'

# Replace INVITE_LINK with the invite link to the group or channel
invite_link = 'INVITE_LINK'

# Define the /start command handler
@app.on_message(filters.command('start'))
def start_handler(client, message):
    user = message.from_user
    chat_id = message.chat.id

    # Create an inline keyboard with a "Join Group" button
    keyboard = [[InlineKeyboardButton("Join Group", url=invite_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message to the user with the inline keyboard
    client.send_message(chat_id=chat_id, text=f"Hi {user.first_name}! Please join the group {group_username} to use this bot.", reply_markup=reply_markup)

# Define the callback query handler for the "Join Group" button
@app.on_callback_query(filters.regex('^join_group$'))
def join_group_handler(client, callback_query):
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id

    # Check if the user is already a member of the group
    is_member = client.get_chat_member(chat_id, user_id).status

    if is_member == 'left':
        # If the user has left the group, send a message with the invite link and ask them to join
        client.send_message(chat_id=user_id, text=f"Please join the group {group_username} to use this bot.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Join Group", url=invite_link)]]))
    elif is_member == 'kicked':
        # If the user has been kicked from the group, send a message informing them that they cannot use the bot
        client.send_message(chat_id=user_id, text="Sorry, you have been kicked from the group and cannot use this bot.")
    else:
        # If the user is already a member of
