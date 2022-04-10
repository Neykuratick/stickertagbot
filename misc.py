from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import settings


class RedisDatabases:
    STICKERS = 'STICKERS'
    USERS = 'USERS'


API_TOKEN = settings.BOT_TOKEN
bot = Bot(token=API_TOKEN)


storage = RedisStorage2(settings.REDIS_HOST, settings.REDIS_PORT, db=5, pool_size=10, prefix='my_fsm_key')
dp = Dispatcher(bot, storage=storage)
