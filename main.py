import json
import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (
    InlineQuery,
    Message,
)
from aiogram.utils import executor

from misc import dp, bot
from stickers import stickers, CustomSticker

logging.basicConfig(level=logging.DEBUG)


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query or 'echo'

    if text == 'echo':
        results = await stickers.get_all()
    else:
        results = await stickers.get(alias=text)

    await bot.answer_inline_query(inline_query.id, results=results, cache_time=1)


class Form(StatesGroup):
    sticker = State()
    alias = State()


@dp.message_handler(commands='add')
async def cmd_start(message: Message):
    await Form.sticker.set()

    await message.reply("Hi there! Send a sticker")


@dp.message_handler(state=Form.sticker, content_types=["sticker"])
async def process_sticker(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        sticker = CustomSticker(
            unique_id=message.sticker.file_unique_id,
            file_id=message.sticker.file_id
        )

        data['sticker'] = json.dumps(dict(sticker))

    await Form.next()
    await message.answer('Send alias')


@dp.message_handler(state=Form.sticker)
async def process_sticker(message: types.Message):
    await message.answer('Send sticker!')


@dp.message_handler(state=Form.alias)
async def process_sticker(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        sticker = CustomSticker(**json.loads(data['sticker']))
        await stickers.add(alias=message.text, file_id=sticker.file_id, unique_id=sticker.unique_id)

    await state.finish()
    await message.answer('Sticker saved!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
