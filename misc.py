from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import settings


class RedisDatabases:
    STICKERS = 'STICKERS'
    USERS = 'USERS'


API_TOKEN = settings.bot_token
bot = Bot(token=API_TOKEN)


storage = RedisStorage2('localhost', 6379, db=5, pool_size=10, prefix='my_fsm_key')
dp = Dispatcher(bot, storage=storage)
