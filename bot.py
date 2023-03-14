
import logging
from telethon import TelegramClient
from config import Config

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    plugins = dict(
        root="plugins"
    )
    client = TelegramClient(
        "ShowJson",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        session_name="session",
        plugins=plugins,
        workers=100
    )
    client.start(bot_token=Config.BOT_TOKEN)
