import json

import aioredis as aioredis
from pydantic import BaseModel
from aiogram.types import InlineQueryResultCachedSticker

from config import settings
from misc import storage, RedisDatabases


class CustomSticker(BaseModel):
    unique_id: str
    file_id: str
    alias: str | None


class StickerStorage:
    def __init__(self):
        self.session = aioredis.from_url(
            settings.redis_url + RedisDatabases.STICKERS,
            decode_responses=True
        )

    async def add(self, unique_id: str, file_id: str, alias: str):
        sticker = CustomSticker(unique_id=unique_id, file_id=file_id, alias=alias)

        async with self.session.client() as client:
            await client.execute_command('lpush', alias, json.dumps(dict(sticker)))

    async def get(self, alias: str) -> list[InlineQueryResultCachedSticker]:
        returning_stickers = []

        async with self.session.client() as client:
            llen = await client.execute_command('llen', alias)
            raw_stickers = await client.execute_command('lrange', alias, 0, llen)
            raw_stickers = [CustomSticker(**json.loads(sticker)) for sticker in raw_stickers]

        for sticker in raw_stickers:
            sticker = InlineQueryResultCachedSticker(
                id=sticker.unique_id,
                sticker_file_id=sticker.file_id
            )

            returning_stickers.append(sticker)

        return returning_stickers

    @staticmethod
    async def get_all():
        returning_stickers = []

        # todo

        return returning_stickers


stickers = StickerStorage()
