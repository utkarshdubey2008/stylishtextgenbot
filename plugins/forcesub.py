
from telethon import TelegramClient, events
from telethon.types import InlineKeyboardButton, InlineKeyboardMarkup

# Replace YOUR_API_ID and YOUR_API_HASH with your API ID and API Hash
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# Replace GROUP_OR_CHANNEL_USERNAME with the username of the group or channel you want to force join
group_username = 'GROUP_OR_CHANNEL_USERNAME'

# Replace INVITE_LINK with the invite link to the group or channel
invite_link = 'INVITE_LINK'

client = TelegramClient('my_bot', api_id, api_hash)

# Define the /start command handler
@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    user = await event.get_sender()
    chat_id = event.chat_id

    # Create an inline keyboard with a "Join Group" button
    keyboard = [[InlineKeyboardButton("Join Group", url=invite_link)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message to the user with the inline keyboard
    await client.send_message(chat_id=chat_id, message=f"Hi {user.first_name}! Please join the group {group_username} to use this bot.", buttons=reply_markup)

# Define the callback query handler for the "Join Group" button
@client.on(events.CallbackQuery(pattern='join_group'))
async def join_group_handler(event):
    chat_id = event.chat_id
    user_id = event.sender_id

    # Check if the user is already a member of the group
    is_member = await client.get_participants(chat_id, ids=[user_id])

    if not is_member:
        # If the user is not a member of the group, send a message with the invite link and ask them to join
        await client.send_message(chat_id=user_id, message=f"Please join the group {group_username} to use this bot.", buttons=InlineKeyboardMarkup([[InlineKeyboardButton("Join Group", url=invite_link)]]))
    else:
        # If the user is already a member of the group, continue with the bot's functionality
        await event.answer('You are already a member of the group!', show_alert=True)

client.start()
client.run_until_disconnected()
